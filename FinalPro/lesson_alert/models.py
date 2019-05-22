from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    Lesson_List = [
        ('第一節','8:10-9:00'),
        ('第二節','9:10-10:00'),
        ('第三節','10:10-11:00'),
        ('第四節','11:10-12:00'),
        ('第五節','13:10-14:00'),
        ('第六節','14:10-15:00'),
        ('第七節','15:10-16:00'),
        ('第八節','16:10-17:00'),
        ('第九節','17:10-18:00'),
        ('第十節','18:10-19:00'),
        ('第十一節','19:10-20:00'),
        ('第十二節','20:10-21:00'),]
    Week_List = [
        ('星期一','星期一'),
        ('星期二','星期二'),
        ('星期三','星期三'),
        ('星期四','星期四'),
        ('星期五','星期五'),
        ('星期六','星期六'),
        ('星期日','星期日'),]
    
    Name = models.CharField(max_length=255,verbose_name='課程名稱',default="")
    User = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="使用者",default="")
    Week = models.CharField(max_length=20,verbose_name='星期幾',choices=Week_List,default="")
    Lesson = models.CharField(max_length=20,verbose_name='第幾節',choices=Lesson_List,default="")