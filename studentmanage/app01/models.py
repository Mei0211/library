from django.db import models


# Create your models here.
class User(models.Model):  #用户表
    user_name=models.CharField(max_length=20,null=False)#姓名
    user_id=models.CharField(max_length = 20)#id
    user_account=models.CharField(max_length = 20,primary_key=True)#电话
    user_password=models.CharField(max_length = 20)#用户密码


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False)
    address = models.CharField(max_length=64, null=False)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10.01)
    inventory = models.IntegerField(verbose_name="库存数")
    sale_num = models.IntegerField(verbose_name="借出数")
    publisher = models.ForeignKey(to='Publisher', on_delete=models.CASCADE)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    # mysql中的多对多表查询
    book = models.ManyToManyField(to='Book')