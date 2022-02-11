from django.shortcuts import render
from .models import Group

# Create your views here.

def addgroup(request):

    form = GroupForm(request.POST or None)
    object_list = Group.objects.all()
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = GroupForm()
    return render(request,'group/addgroup.html',{"form":form,"obj_list":object_list})

from django.shortcuts import render
from .forms import GroupForm
# Create your views here.

def add_group(request):
    # return render(request,"group/add-group.html",{"form":form})
    # return render(request,"group/group_page.html",{"form":form})
    return render(request,"group/group.html",{"form":form,"objects_list":obj})
