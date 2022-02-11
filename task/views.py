from django.shortcuts import render

# Create your views here.

def addtask(request):
    form = TaskForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = TaskForm()
    return render(request,'task/addtask.html')

from django.shortcuts import render
from .forms import TaskForm
# Create your views here.

def add_task(request):
    return render(request,"task/add-task.html",{"form":form})
    # return render(request,"task/taskpage.html",{"form":form})
