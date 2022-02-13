from django.urls import path,include
from . import views

urlpatterns = [
    path('addproject',views.addproject,name='addproject'),
    path('delete-project/<str:pk>',views.deleteProject,name='delete-project'),
    path('update-project/<str:pk>',views.updateProject,name='update-project'),
]