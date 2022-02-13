from django.urls import path,include
from  . import views

urlpatterns = [
    path('',views.base,name='base'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('user',views.user,name='user'),
    path('employee',views.employee,name='employee'),
    path('delete-user/<str:pk>',views.deleteUser,name='delete-user'),
    path('update-user/<str:pk>',views.updateUser,name='update-user'),
    path('register/', views.register,name="register"),
    path('login/', views.user_login,name="user_login"),
]