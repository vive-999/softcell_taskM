from django.urls import path,include
from  . import views

urlpatterns = [
    path('addincident',views.addincident,name='addincident'),
]