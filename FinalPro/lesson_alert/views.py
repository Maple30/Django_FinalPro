from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required, login_required
from .forms import UserCreationForm, LessonsForm
from django.contrib import messages
from lesson_alert.models import Category
from django.http import HttpResponse
from django.contrib.auth.views import auth_logout
from django.core.mail import send_mail
from django.conf import settings
import datetime

# Create your views here.
def index(request):
    User = request.user 
    print(request.user,'111')

    if str(request.user) == "AnonymousUser":
        messages.add_message(request, messages.INFO, '需要註冊才能使用喔')
    

    return render(request,'base.html', locals())

class UserCreate(generic.CreateView):
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        messages.success(self.request, '帳戶已創立')
        return reverse('login')

@login_required
def add_lesson(request):
    if request.method == "POST":
        
        form = LessonsForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.User = request.user
            lesson.save()
            messages.success(request, '課程已新增')
            return redirect('index')
    else:
        form = LessonsForm()
    return render(request, 'forms.html', {'form': form})
@login_required
def lesson_list(request):
    List = Category.objects.filter(User__username=request.user)
    User = request.user
    days = [1,2,3,4,5,6,7]
    # flag = 0
    # def LessonAdded():
    #     flag = 1
    # def LessonNotAdded():
    #     flag = 0
    List = Category.objects.filter(Lesson='第一節')
    print(List)
    day = datetime.datetime.today().strftime('%A')
    print(day)
    print(datetime.datetime.now().strftime('%H:%M'))
    send_mail('Subject here', 'Here is the message.', 'toolsdesu@gmail.com', ['kp3344567@gmail.com'], fail_silently=False)
    return render(request,'lesson_list.html',locals())
# def loged_out(request):
#     logout(request)
#     return redirect('/logout')
     