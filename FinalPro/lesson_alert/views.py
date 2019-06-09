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

# Create your views here.
def index(request):
    return render(request,'base.html', {})

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
    print(request.user)
    for i in List:
        print(i.Lesson)
        print(i.Week)
    return render(request,'lesson_list.html',locals())
# def loged_out(request):
#     logout(request)
#     return redirect('/logout')
     