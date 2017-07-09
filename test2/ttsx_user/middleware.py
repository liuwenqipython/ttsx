#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

#判断是否登录
def islogin(func):
    def func1(request,*args,**kwargs):
        if request.session.get('islogin') != True:
            return redirect('/login/')
            #return HttpResponse(request.session['islogin'])
        else:
            return func(request,*args,**kwargs)
    return func1



