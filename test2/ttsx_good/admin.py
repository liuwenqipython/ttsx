from django.contrib import admin
from models import Goodsinfo
# Register your models here.

class Goodsinfoadmin(admin.ModelAdmin):
    list_display = ['id','name','pic','price','gclick','typegood']

admin.site.register(Goodsinfo,Goodsinfoadmin)