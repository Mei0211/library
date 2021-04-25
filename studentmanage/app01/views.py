from django.shortcuts import render, redirect
from app01 import models

from app01.models import *


# Create your views here.
def login(request):#登录
    return render(request, 'login.html')

def register(request):  # 学生注册
    name_r = request.POST.get("name")  # 获取学生输入的姓名
    id_r = request.POST.get("id")  # 获取学生输入的学号
    tel_r = request.POST.get("telephone")
    pwd_r = request.POST.get("password")
    result1 = User.objects.filter(user_account=tel_r)  # 在用户表中搜索该用户名的记录
    context = {}
    if len(result1) == 1:  # 判断该账户是否存在(即判断是否注册过)，如果后台存在记录，则返回相应的提示语句
        context["info"] = "已注册！！！"
        context["status"] = 0  #零表示注册失败
        return render(request, 'login.html', context=context)
    else:  #该账户是新用户
            User.objects.create(user_name=name_r,user_id=id_r, user_password=pwd_r,user_account=tel_r)#用create为user表添加一条记录
            context["info"] = "注册成功！"
            context["status"] = 1  #1表示注册成功
            return render(request, 'login.html', context=context)

def login_judge(request):#登入判定
    tel = request.POST.get("telephone")#获取前端输入的账户（手机号）
    pwd = request.POST.get("password")
    result1 = User.objects.filter(user_account=tel)#在user表里检索是否存在该账户
    if len(result1) == 1:  # 判断后台是否存在该用户，有则进一步判断密码是否正确
        password = result1[0].user_password  # 获取后台的密码
        if pwd == password :  # 将用户输入的密码和后台密码进行比对,如何正确，判断该账户身份
                return render(request, 'book_list.html')  # 跳转

        else:  # 如果不一致则返回相应提示语句
            context = {
                "info": "密码错误！！！",
                "status": 2
            }
            return render(request, 'login.html', context=context)  # 密码错误回到登入界面
    else:  # 如果不存在该用户则提示
        context = {
            "info": "该账户不存在！！！",
            "status": 3
        }
        return render(request, 'login.html', context=context)  # 账户不存在则继续回到登入界面


def add_publisher(request):
    if request.method == "POST":
        # 获取表单提交的内容
        publisher_name = request.POST.get("name")
        publisher_address = request.POST.get("address")
        # 保存到数据库
        Publisher.objects.create(name=publisher_name, address=publisher_address)
        return redirect("/publisher_list")

    return render(request, 'add_publisher.html')


def publisher_list(request):
    # 查询数据库中的所有信息
    publisher_list = Publisher.objects.all()
    return render(request, "publisher_list.html", {"publisher_obj_list": publisher_list})


def edit_publisher(request):
    if request.method == "POST":
        # 1. 获取表单提交的内容
        id = request.POST.get('id')
        name = request.POST.get('name')
        address = request.POST.get('address')
        # 2. 根据id去数据库中查找对象
        publisher_obj = Publisher.objects.get(id=id)
        # 3. 修改
        publisher_obj.name = name
        publisher_obj.address = address
        publisher_obj.save()
        # 4. 重定向到出版社列表
        return redirect('/publisher_list/')
    else:
        # 获得id
        id = request.GET.get('id')
        # 去数据库中查找相应的数据
        publisher_obj = Publisher.objects.get(id=id)
        publisher_obj_list = Publisher.objects.all()
        # 返回页面
        return render(request, 'edit_publisher.html',
                      {"publisher_obj": publisher_obj, "publisher_obj_list": publisher_obj_list})


def delete_publisher(request):
    # 获取id
    id = request.GET.get("id")
    Publisher.objects.filter(id=id).delete()
    return redirect("/publisher_list")


def book_list(request):
    book_obj_list = Book.objects.all()
    return render(request, 'book_list.html', {"book_obj_list": book_obj_list})

def search_book(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        book_result = Book.objects.filter(name=book_name)
        return render(request,'search_book.html',{"book_obj_list":book_result})
    else:
       return redirect('/book_list/')
    

def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        inventory = request.POST.get('inventory')
        sale_num = request.POST.get('sale_num')
        publisher_id = request.POST.get('publisher_id')
        Book.objects.create(name=name, price=price, inventory=inventory, sale_num=sale_num,
                                   publisher_id=publisher_id)
        return redirect('/book_list/')
    else:
        # 1.获取所有出版社信息
        publisher_obj_list = Publisher.objects.all()

        return render(request, 'add_book.html', {"publisher_obj_list": publisher_obj_list})


def edit_book(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        book_obj = Book.objects.filter(id=id).first()
        publisher_list = Publisher.objects.all()
        return render(request, 'edit_book.html', {'book_obj': book_obj, 'publisher_list': publisher_list})
    else:
        # 获取表单提交过来的内容
        id = request.POST.get('id')
        name = request.POST.get('name')
        inventory = request.POST.get('inventory')
        price = request.POST.get('price')
        sale_num = request.POST.get('sale_num')
        publisher_id = request.POST.get('publisher_id')
        # 查询数据库进行更新
        Book.objects.filter(id=id).update(name=name, inventory=inventory,
                                                 price=price, sale_num=sale_num, publisher_id=publisher_id)
        # 重定向到book_list
        return redirect("/book_list")


def delete_book(request):
    # 获取id
    id = request.GET.get("id")
    Book.objects.filter(id=id).delete()
    return redirect("/book_list")


def author_list(request):
    ret_list = []
    author_obj_list = Author.objects.all()
    for author_obj in author_obj_list:
        book_obj_list = author_obj.book.all()
        ret_dic = {}
        ret_dic['author_obj'] = author_obj
        ret_dic['book_list'] = book_obj_list
        ret_list.append(ret_dic)
    return render(request, 'author_list.html', {'ret_list': ret_list})


def add_author(request):
    if request.method == 'GET':
        # 1获取所有的图书
        book_obj_list = Book.objects.all()
        # 2返回页面
        return render(request, 'add_author.html', {'book_obj_list': book_obj_list})
    else:
        # 1.获取表单提交过来的数据
        name = request.POST.get('name')
        book_ids = request.POST.getlist('books')
        # 2 保存数据库
        author_obj = Author.objects.create(name=name)  # 创建对象
        author_obj.book.set(book_ids)  # 设置关系
        # 3 重定向到列表页面
        return redirect('/author_list/')


def edit_author(request):
    if request.method == 'GET':
        # 1.获取id
        id = request.GET.get('id')
        # 2查询对象和所有的图书
        author_obj = Author.objects.get(id=id)  # id查出所有作者
        book_obj_list = Book.objects.all()  # 查出作者的所有图书
        # 3返回页面
        return render(request, 'edit_author.html',
                      {'author_obj': author_obj, 'book_obj_list': book_obj_list})
    else:
        # 保存修改的数据
        # 1.获取表单提交过来的内容
        id = request.POST.get('id')
        name = request.POST.get('name')
        book_ids = request.POST.getlist('books')
        # 2,根据id 查找对象，并修改
        author_obj = Author.objects.filter(id=id).first()
        author_obj.name = name
        author_obj.book.set(book_ids)
        author_obj.save()
        # 3.重定向到作者列表
        return redirect('/author_list/')


def delete_author(request):
    # 1 获取id
    id = request.GET.get("id")
    # 2删除作者
    Author.objects.filter(id=id).delete()
    # 重定向作者列表
    return redirect("/author_list")
