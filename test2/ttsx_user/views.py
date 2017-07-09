#coding=utf-8

from django.shortcuts import render,redirect
from models import ttsx_user
from django.http import HttpResponse,JsonResponse
from hashlib import sha1
from middleware import islogin

# Create your views here.

#注册界面
def register(request):
    return render(request,'ttsx_user/register.html',{'centent':'注册'})
#判断用户名是否存在  ajax
def register_cheak(request):
    name = request.GET.get('name')
    eorr = ttsx_user.objects.filter(name=name).count()
    return JsonResponse({'eorr':eorr})
#接收注册数据
def register_verify(request):
    centent = request.POST
    name = centent.get('name')
    pwd = centent.get('pwd')
    email = centent.get('email')

    s1 = sha1()
    s1.update(pwd)
    pwd_sha1 = s1.hexdigest()

    t = ttsx_user()
    t.name = name
    t.pwd = pwd_sha1
    t.email = email
    t.save()
    return redirect('/login/')

#登录界面
def login(request):
    if request.COOKIES.has_key('name'):
        name = request.COOKIES['name']
        #return HttpResponse(name)
        return render(request,'ttsx_user/login.html',{'name':name})
    else:
        return render(request, 'ttsx_user/login.html')

#登录验证
def login_cheak(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    box = request.POST.get('box')

    s1 = sha1()
    s1.update(pwd)
    pwd_sha1 = s1.hexdigest()
    #return HttpResponse(box)
    if name!='' and pwd!='':
        t = ttsx_user.objects.filter(name=name)
        if t[0].name==name and t[0].pwd==pwd_sha1:
            reponse = redirect('/info/')
            reponse.set_cookie('name',name)
            request.session['name'] = name
            request.session['islogin'] = True
            if box=="1":
                request.session['name']=name
            return reponse
        else:
            return render(request,'ttsx_user/login.html',{"eorr":'密码错误'})
            #return JsonResponse({'eorr':'no'})

#用户中心
@islogin
def info(request):
    name = request.session.get('name')
    users = ttsx_user.objects.get(name=name)
    #return HttpResponse(users[0].name)
    return render(request,'ttsx_user/info.html',{'users':users,'centent':'用户中心','top':1})

@islogin
def order(request):
    return render(request,'ttsx_user/order.html',{'centent':'用户中心','top':1})

@islogin
def site(request):
    name = request.session.get('name')
    users = ttsx_user.objects.get(name=name)
    return render(request,'ttsx_user/site.html',{'users':users,'centent':'用户中心','top':1})

def site_cheak(request):
    uname = request.session.get('name')
    users = ttsx_user.objects.get(name=uname)

    name = request.POST.get('name')
    adress = request.POST.get('adress')
    phone = request.POST.get('phone')

    users.name = name
    users.adress = adress
    users.phone = phone
    users.save()
    return redirect('/index/')
    #return HttpResponse(name)


def login_stop(request):
    #name = request.session.get('name')
    request.session.flush()
    return redirect('/login/')














