from . import views
from django.urls import path
from .forms import LoginForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home , name='home'),
    path('about/', views.about , name='about'),
    path('contact/', views.contact , name='contact'),
    path('portfolio', views.portfolio , name='portfolio'),
    path('service/', views.service , name='service'),
    path('team/', views.team , name='team'),
    path('message/', views.message , name='message'),
    path('logout/', views.logout_user, name='logout'),
     path('papp/login', auth_views.LoginView.as_view(template_name='papp/login.html', 
     authentication_form=LoginForm),name='login'),
    ]