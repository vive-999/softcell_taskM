from django.urls import path,include
from  . import views

urlpatterns = [
    path('addgroup',views.addgroup,name='addgroup'),
    path('delete-group/<str:pk>',views.deleteGroup,name='delete-group'),
    path('update-group/<str:pk>',views.updateGroup,name='update-group'),
]