from django.urls import path,include
from  . import views

urlpatterns = [
    path('addgroup',views.addgroup,name='addgroup'),
]