"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from pages import views

urlpatterns = [
    path('', views.register, name='register'),          
    path('register/', views.register, name='register'), 
    path('login/', views.login_view, name='login'),     
    path('logout/', views.logout_view, name='logout'),  
    path('home/', views.home_view, name='home'), 
    path('about/', views.about, name='about'),
    path("predictions/", views.predictions_view, name="predictions"),    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('insights/', views.insights, name='insights'), 
    path('contact/', views.contact, name='contact'),       
]
