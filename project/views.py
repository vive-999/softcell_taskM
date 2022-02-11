from django.shortcuts import render
from .models import Project

# Create your views here.

def addproject(request):
    form = ProjectForm(request.POST or None)
    object_list = Project.objects.all()
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = ProjectForm()
    return render(request,'project/addproject.html',{"form":form,"obj_list":object_list})

from django.shortcuts import render
from .forms import ProjectForm

# Create your views here.
def add_projects(request):
    # return render(request,"project/add-project.html",{"form":form})
    return render(request,"project/project_page.html",{"form":form})