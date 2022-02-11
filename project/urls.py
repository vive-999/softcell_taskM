from django.urls import path,include
from . import views

urlpatterns = [
    path('addproject',views.addproject,name='addproject'),
]