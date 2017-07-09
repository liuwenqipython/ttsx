#coding=utf-8

from django.db import models
from tinymce.models import HTMLField
# Create your models here.

'''
#商品分类 一类
class Typegoods(models.Model):
    Typename = models.CharField(max_length=20)    #商品类名称
    isdelte = models.BooleanField(default=False)  #标记

    def __str__(self):
        return self.Typename.encode('utf-8')

#商品 多类
class Goods(models.Model):
    title = models.CharField(max_length=20)  #商品名称
    pic = models.ImageField(upload_to='goods/')  #商品图片路径
    price = models.DecimalField(max_digits=5,decimal_places=2)  #商品价格
    units = models.CharField(max_length=20)   #单位
    describe = models.CharField(max_length=200)
    referral = HTMLField()  #商品介绍 富文本编辑框
    isdelte = models.BooleanField(default=False)
    typegood = models.ForeignKey('Typegoods')  #关联关系

'''

class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=10)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle.encode('utf-8')


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='goods/')
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    gclick = models.IntegerField()
    gunit = models.CharField(max_length=10)
    isDelete = models.BooleanField(default=False)
    gsubtitle = models.CharField(max_length=200)
    gkucun = models.IntegerField(default=100)    #库存
    gcontent = HTMLField()
    gtype = models.ForeignKey('TypeInfo')

