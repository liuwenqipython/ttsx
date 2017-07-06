#coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^register/$',views.register),  #用户注册界面
    url(r'^register_cheak/$',views.register_cheak), #保存用户输入的数据到数据库
    url(r'^login/$',views.login),  #用户登录界面
    url(r'^login_cheak/$',views.login_cheak), #验证用户名密码
    url(r'^info/$',views.info),  #用户中心
    url(r'^order/$',views.order), #订单
    url(r'^site/$',views.site),  #收货地址
    url(r'^site_cheak/$',views.site_cheak), #保存收货地址到数据库
]