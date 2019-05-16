from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    Name = models.CharField(max_length=255,verbose_name='課程名稱')
    User = models.ForeignKey(User, on_delete=models.CASCADE,default="",verbose_name="使用者")
    Time = models.CharField(max_length=20,verbose_name='課程時間')