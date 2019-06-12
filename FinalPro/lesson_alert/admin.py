from django.contrib import admin
from lesson_alert.models import Category
import django
# Register your models here.

admin.site.register(Category)


#for i in Category.objects.all():
#    print(i.Name)


# print(Category.objects.all())
