from django.urls import path,include
from  . import views

urlpatterns = [
    path('',views.base,name='base'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('user',views.user,name='user'),
    path('register/', views.register,name="register"),
    path('login/', views.user_login,name="user_login"),
]