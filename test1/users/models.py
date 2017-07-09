
from django.db import models

# Create your models here.

class ttsxinfo(models.Model):
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(default='',max_length=11)
    address = models.CharField(default='',max_length=100)
    code = models.CharField(default='',max_length=6)


