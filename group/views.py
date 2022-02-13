from django.shortcuts import render
from .models import Group
from .forms import GroupForm

# Create your views here.

def addgroup(request):

    form = GroupForm(request.POST or None)
    object_list = Group.objects.all()
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        form = GroupForm()
    return render(request,'group/addgroup.html',{"form":form,"obj_list":object_list})




