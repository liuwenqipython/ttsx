from django.shortcuts import render
from models import TypeInfo,GoodsInfo
from django.http import HttpResponse
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    typelist = TypeInfo.objects.all()
    for type1 in typelist:
        goodslist = type1.goodsinfo_set.order_by('-id')
        #centent=[{'typelist':typelist,'goodslist':goodslist}]
    return HttpResponse(type1)
    #return render(request,'users/index.html',centent)

def goodslist(request):
    type1 = TypeInfo.objects.get(id=1)
    glist = type1.goodsinfo_set.order_by('-id')[0:2]
    glists = type1.goodsinfo_set.all()
    paginator = Paginator(glists, 15)
    pagelist = paginator.page_range
    #page = paginator.page()
    centext = {'type1':type1,'glist':glist,'glists':glists,'paginator':paginator,'pagelist':pagelist}
    return render(request,'users/list.html',centext)

def detail(request):
    return render(request,'users/detail.html')