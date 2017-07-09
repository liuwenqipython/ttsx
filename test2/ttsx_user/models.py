#coding=utf-8
from django.db import models

# Create your models here.

#模型类
class ttsx_user(models.Model):
    name = models.CharField(max_length=20)  #用户名
    pwd = models.CharField(max_length=50)  #密码
    email = models.CharField(max_length=50)  #邮箱
    phone = models.CharField(max_length=11)
    adress = models.CharField(max_length=100)

