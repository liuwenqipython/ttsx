#coding=utf-8
from django.shortcuts import render
from models import Typeinfo,Goodsinfo
from django.http import HttpResponse
from django.core.paginator import Paginator
# Create your views here.

#首页
def index(request):
    name = request.COOKIES['name']
    types = Typeinfo.objects.all()
    list=[]
    for type in types:
        good = type.goodsinfo_set.order_by('-id')[0:4]
        goods = type.goodsinfo_set.order_by('gclick')[0:4]
        list.append({'good':good,'goods':goods,'type':type})
    return render(request,'ttsx_good/index.html',{'centent':'首页','name':name,'list':list})
    #return HttpResponse(goods[0].pic)

#商品列表
def list(request,bid):
    name = request.COOKIES['name']
    type = Typeinfo.objects.get(id=bid)
    goods = type.goodsinfo_set.all()
    paginator = Paginator(goods, 15)
    page = paginator.page(1)
    good = type.goodsinfo_set.order_by('-id')[0:2]
    return render(request,'ttsx_good/list.html',{'name':name,'centent':'商品列表','type':type,'goods':goods,'good':good,'paginator':paginator,'page':page})

def detail(request,bid):
    name = request.COOKIES['name']
    type = Typeinfo.objects.get(id=bid)
    goods = type.goodsinfo_set.order_by('-id')[0:1]
    good = type.goodsinfo_set.order_by('-id')[0:2]
    return render(request,'ttsx_good/detail.html',{'centent':'商品详情','name':name,'type':type,'goods':goods,'good':good})