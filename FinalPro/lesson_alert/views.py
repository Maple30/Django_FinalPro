from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User

from .forms import UserCreationForm

# Create your views here.


def index(request):
    return render(request,'base.html', {})

class UserCreate(generic.CreateView):
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        # messages.success(self.request, '帳戶已創立')
        return reverse('login')