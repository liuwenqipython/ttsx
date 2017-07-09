#coding=utf-8

from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Typeinfo(models.Model):
    typename = models.CharField(max_length=20)
    isdelete = models.BooleanField(default=False)

class Goodsinfo(models.Model):
    name = models.CharField(max_length=20)
    pic = models.ImageField(upload_to='goods/')
    price = models.DecimalField(max_digits=5,decimal_places=2)
    gclick = models.IntegerField()
    unit = models.CharField(max_length=10)
    isdelete = models.BooleanField(default=False)
    tilte = models.CharField(max_length=200)
    kucun = models.IntegerField(default=100)
    describe = HTMLField()
    typegood = models.ForeignKey('Typeinfo')