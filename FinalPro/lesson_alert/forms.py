from django import forms
from .models import Category
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.db.models import EmailField
from django.utils.translation import ugettext_lazy as _ 


class UserCreationForm(UserCreationForm):
    email = EmailField(_('email address'))

    class Meta:
        fields = ('username','email')
        model = User
        field_classes = {'username': UsernameField}

class LessonsForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('Name', 'Week','Lesson')
