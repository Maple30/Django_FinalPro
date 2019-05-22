from django.urls import path, include


from . import views

urlpatterns = (
    path('', views.index, name='index'),
    path('sign-up', views.UserCreate.as_view(), name='sign_up'),
    path('add_lesson', views.add_lesson, name = 'add_lesson'),
)