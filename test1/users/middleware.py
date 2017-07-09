#coding=utf-8
import views
from django.shortcuts import render,redirect
#判断是否登录-装饰器
def islogin(func):
    def func1(request):
        if request.session['name'] ==True:
            return func()
        else:
            return redirect('/login/')
    return func

#记录用户当前的路径
class urlPathmiddleware():
    def process_request(self,request):
        path = request.get_full_path() #带参数
        #当是登录/注册不用记录
        path1 = request.path
        if path1 not  in ['/login/']:

            request.session['user_path']=path

#class TestMeddleware():
