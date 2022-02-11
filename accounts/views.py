
import re
from django.shortcuts import redirect, render
from django.shortcuts import render
from .forms import UserCreationForm, UserLoginForm,EmployeeCreatiionForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User





def base(request):
    print(request.user)
    return render(request,'accounts/base.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def user(request):
    form = UserCreationForm()
    employeeform=EmployeeCreatiionForm()
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        employeeform=EmployeeCreatiionForm(request.POST)
        name = User.objects.get(id=request.POST.get("user"))
        print(f"The name of the user is {user}")
        print(employeeform.__getattribute__)
        print(employeeform.__getitem__)
        if form.is_valid():
            form.save()
        if employeeform.is_valid():
            employeeform.save()
            return redirect('base')


 
    return render(request,'accounts/user.html',{'form':form, 'employeeform':employeeform})

def register(request,*args,**kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        print("user Created")
        return  HttpResponseRedirect("/")
    # return  render(request,'accounts/register.html',{'form':form})
    return  render(request,'accounts/register_page.html',{'form':form})


def user_login(request,*args,**kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        print("user Logged In")
        return  HttpResponseRedirect("/")
    return  render(request,'accounts/login_page.html',{'form':form})

