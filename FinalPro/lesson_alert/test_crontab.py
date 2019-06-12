import random

from django.core.cache import cache
from django.core.mail import send_mail
from django.http import request
import datetime
from lesson_alert.models import Category

def Earlyeight(request):
        List = Category.objects.filter(Lesson='第一節')
        for i in List:
              if(i.Lesson == '')  
        send_mail('Subject here', 'Here is the message.', 'toolsdesu@gmail.com', ['kp3344567@gmail.com'], fail_silently=False)