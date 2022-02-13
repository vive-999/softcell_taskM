from django.shortcuts import redirect, render
from .models import Project
from .forms import ProjectForm

# Create your views here.

def addproject(request):
    form = ProjectForm()
    all_projects = Project.objects.all()
    if request.method=="POST":
        form = ProjectForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('addproject')
    return render(request,'project/addproject.html',{"form":form,"all_projects":all_projects})

def deleteProject(request, pk):
    emp =Project.objects.get(id=pk)
    print(emp)
    if request.method =="POST":
        emp.delete()
        return redirect('addproject')
    return render(request,'project/delete.html',{'emp':emp})

def updateProject(request, pk):
    emp = Project.objects.get(id=pk)
    form = ProjectForm(instance=emp)
    if request.method=="POST":
        form = ProjectForm(request.POST,instance=emp)
        if form.is_valid():

            form.save()
            return redirect('addproject')
    context={'form':form}
    return render(request,'project/update.html',context)



