#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from models import ttsxinfo  #导入模型类
from hashlib import sha1
# Create your views here.

#用户注册界面
def register(request):

    return render(request,'users/register.html')
#保存到数据库
def register_cheak(request):
    uname = request.POST.get('name')
    upwd =request.POST.get('pwd')
    uemail = request.POST.get('email')
    #密码加密
    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()
    #保存到数据库
    t = ttsxinfo()
    t.name = uname
    t.pwd = upwd_sha1
    t.email = uemail
    t.save()
    return render(request,'users/login.html')
#用户登录界面
def login(request):
    return render(request,'users/login.html',{'name':name})
#验证用户名密码
def login_cheak( request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    box = request.POST.get('box')

    if pwd=='' or name=='':
        return redirect('/login/')
    else:
        s1 = sha1()
        s1.update(pwd)
        pwd_sha = s1.hexdigest()

        t1 = ttsxinfo.objects.filter(name=name)
        if name==t1[0].name and pwd_sha == t1[0].pwd:
            request.session['islogin']=True
            reponse = render(request,'users/index.html')
            reponse.set_cookie('name',name)
            return reponse
        else:
            return redirect('/login/')

    #return HttpResponse(pwd_sha)
#用户中心
def info(request):
    name = request.COOKIES['name']
    t1 = ttsxinfo.objects.get(name=name)
    #centext = {'t1':t1}
    #return HttpResponse(t1.pwd)
    return render(request,'users/user_center_info.html',{'t1':t1})
#订单
def order(request):
    return render(request,'users/user_center_order.html')
#收货地址
def site(request):
    name = request.COOKIES['name']
    t1 = ttsxinfo.objects.get(name=name)
    return render(request,'users/user_center_site.html',{'t1':t1})
#保存收货地址到数据库
def site_cheak(request):
    name = request.POST.get('name')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    code = request.POST.get('code')
    #修改数据库数据
    t1 = ttsxinfo.objects.get(name=name)
    t1.name = name
    t1.address = address
    t1.code = code
    t1.phone = phone
    t1.save()
    return HttpResponse('ok')



