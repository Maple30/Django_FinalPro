import random

from django.core.cache import cache
from django.core.mail import send_mail
from django.http import request
import datetime
from lesson_alert.models import Category
Eng2Chi = {'Monday':'星期一','Tuesday':'星期二','Wednesday':'星期三','Thursday':'星期四','Friday':'星期五','Saturday':'星期六','Sunday':'星期日'}
#send_mail('Subject here', 'Here is the message.', 'toolsdesu@gmail.com', ['kp3344567@gmail.com'], fail_silently=False)

def Test():
      send_mail('Subject here', 'Here is the message.', 'toolsdesu@gmail.com', ['kp3344567@gmail.com'], fail_silently=False)

def Eight():
        List = Category.objects.filter(Lesson='第一節')
        day = datetime.datetime.today().strftime('%A')
        key = Eng2Chi[day]
        for i in List:
              if(i.Week == key):
                      i.User.email_user("上課提醒","您在8:10有一堂"+i.Name+'記得去上課喔','toolsdesu@gmail.com', fail_silently=False)
                      print('Send')
def Nine():
        List = Category.objects.filter(Lesson='第二節')
        day = datetime.datetime.today().strftime('%A')
        key = Eng2Chi[day]
        for i in List:
              if(i.Week == key):
                      i.User.email_user("上課提醒","您在9:10有一堂"+i.Name+'記得去上課喔','toolsdesu@gmail.com', fail_silently=False)
                      print('Send')
def Ten():
        List = Category.objects.filter(Lesson='第三節')
        day = datetime.datetime.today().strftime('%A')
        key = Eng2Chi[day]
        for i in List:
              if(i.Week == key):
                      i.User.email_user("上課提醒","您在10:10有一堂"+i.Name+'記得去上課喔','toolsdesu@gmail.com', fail_silently=False)
                      print('Send')
def Eleven():
        List = Category.objects.filter(Lesson='第四節')
        day = datetime.datetime.today().strftime('%A')
        key = Eng2Chi[day]
        for i in List:
              if(i.Week == key):
                      i.User.email_user("上課提醒","您在11:10有一堂"+i.Name+'記得去上課喔','toolsdesu@gmail.com', fail_silently=False)
                      print('Send')
def Thirteen():
        List = Category.objects.filter(Lesson='第五節')
        day = datetime.datetime.today().strftime('%A')
        key = Eng2Chi[day]
        for i in List:
              if(i.Week == key):
                      i.User.email_user("上課提醒","您在13:10有一堂"+i.Name+'記得去上課喔','toolsdesu@gmail.com', fail_silently=False)
                      print('Send')
def Fourteen():
        List = Category.objects.filter(Lesson='第六節')
        day = datetime.datetime.today().strftime('%A')
        key = Eng2Chi[day]
        for i in List:
              if(i.Week == key):
                      i.User.email_user("上課提醒","您在14:10有一堂"+i.Name+'記得去上課喔','toolsdesu@gmail.com', fail_silently=False)
                      print('Send')
def Fifteen():
        List = Category.objects.filter(Lesson='第七節')
        day = datetime.datetime.today().strftime('%A')
        key = Eng2Chi[day]
        for i in List:
              if(i.Week == key):
                      i.User.email_user("上課提醒","您在15:10有一堂"+i.Name+'記得去上課喔','toolsdesu@gmail.com', fail_silently=False)
                      print('Send')
def Sixteen():
        List = Category.objects.filter(Lesson='第八節')
        day = datetime.datetime.today().strftime('%A')
        key = Eng2Chi[day]
        for i in List:
              if(i.Week == key):
                      i.User.email_user("上課提醒","您在16:10有一堂"+i.Name+'記得去上課喔','toolsdesu@gmail.com', fail_silently=False)
                      print('Send')
def Seventeen():
        List = Category.objects.filter(Lesson='第九節')
        day = datetime.datetime.today().strftime('%A')
        key = Eng2Chi[day]
        for i in List:
              if(i.Week == key):
                      i.User.email_user("上課提醒","您在17:10有一堂"+i.Name+'記得去上課喔','toolsdesu@gmail.com', fail_silently=False)
                      print('Send')
def Eighteen():
        List = Category.objects.filter(Lesson='第十節')
        day = datetime.datetime.today().strftime('%A')
        key = Eng2Chi[day]
        for i in List:
              if(i.Week == key):
                      i.User.email_user("上課提醒","您在18:10有一堂"+i.Name+'記得去上課喔','toolsdesu@gmail.com', fail_silently=False)
                      print('Send')
def Nineteen():
        List = Category.objects.filter(Lesson='第十一節')
        day = datetime.datetime.today().strftime('%A')
        key = Eng2Chi[day]
        for i in List:
              if(i.Week == key):
                      i.User.email_user("上課提醒","您在19:10有一堂"+i.Name+'記得去上課喔','toolsdesu@gmail.com', fail_silently=False)
                      print('Send')
def Twanty():
        List = Category.objects.filter(Lesson='第十二節')
        day = datetime.datetime.today().strftime('%A')
        key = Eng2Chi[day]
        for i in List:
              if(i.Week == key):
                      i.User.email_user("上課提醒","您在20:10有一堂"+i.Name+'記得去上課喔','toolsdesu@gmail.com', fail_silently=False)
                      print('Send')