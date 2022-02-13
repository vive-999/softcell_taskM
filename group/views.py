from django.shortcuts import render,redirect
from .models import Group
from .forms import GroupForm

# Create your views here.

def addgroup(request):

    form = GroupForm()
    all_groups = Group.objects.all()
    if request.method=="POST":
        form = GroupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('addgroup')
    return render(request,'group/addgroup.html',{"form":form,"all_groups":all_groups})

def deleteGroup(request, pk):
    emp =Group.objects.get(id=pk)
    print(emp)
    if request.method =="POST":
        emp.delete()
        return redirect('addgroup')
    return render(request,'group/delete.html',{'emp':emp})

def updateGroup(request, pk):
    emp = Group.objects.get(id=pk)
    form = GroupForm(instance=emp)
    if request.method=="POST":
        form = GroupForm(request.POST,instance=emp)
        if form.is_valid():

            form.save()
            return redirect('addgroup')
    context={'form':form}
    return render(request,'group/update.html',context)





