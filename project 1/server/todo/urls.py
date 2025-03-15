from django.urls import path , include
from .import views

urlpatterns = [
    path('', views.home2, name='home2'),
    path('login1/', views.login2, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('',include('django.contrib.auth.urls')),
    path('login/home/',views.home,name='home'),
 

]
