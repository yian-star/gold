from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer

# Create your views here.
from django.db import connection


def index(request):
    # 获取游标对象
    cursor = connection.cursor()
    # 拿到游标对象后执行sql语句
    cursor.execute("select * from user")
    # 获取所有的数据
    rows = cursor.fetchall()
    # 遍历查询到的所有数据
    for row in rows:
        print(row)
    return HttpResponse("查找成功")


def add_customer(request):
    # customer = Customer(nature='网络', company_name='星科技', tax_rate=2.23)
    customer = Customer(nature='实体', company_name='花语', tax_rate=45.23)
    customer.save()
    return HttpResponse("插入成功！")


def query_customer(request):
    # customers = Customer.objects.all()
    # customers = Customer.objects.filter(company_name='星科技')
    #
    # for customer in customers:
    #     print(customer.nature, customer.company_name, customer.tax_rate, customer.regist_time)
    # try:
    #     customer = Customer.objects.get(company_name='星科技1')
    #     print(customer.company_name)
    # except Customer.DoesNotExist:
    #     print("该公司不存在")
    customers = Customer.objects.order_by("-regist_time")
    for customer in customers:
        print(customer.nature, customer.company_name, customer.tax_rate, customer.regist_time)

    return HttpResponse("查找成功！")


def update_view(request):
    customer = Customer.objects.first()
    customer.company_name = '星星科技'
    customer.save()
    return HttpResponse("更新成功！")


def delete_view(request):
    customer = Customer.objects.filter(company_name='花语')
    customer.delete()
    return HttpResponse("删除成功")
