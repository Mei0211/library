# Generated by Django 3.1.7 on 2021-04-02 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=20)),
                ('user_id', models.CharField(max_length=20)),
                ('user_account', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('user_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, default=10.01, max_digits=5)),
                ('inventory', models.IntegerField(verbose_name='库存数')),
                ('sale_num', models.IntegerField(verbose_name='借出数')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('book', models.ManyToManyField(to='app01.Book')),
            ],
        ),
    ]