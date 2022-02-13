
import re
from django.shortcuts import redirect, render
from django.shortcuts import render

from accounts.models import Profile
from .forms import UserCreationForm, UserLoginForm,EmployeeCreatiionForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from group.models import Group
from project.models import Project






def base(request):
    return render(request,'accounts/base.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

#User Creation,Making User Employee,Listing All Employee
def user(request):
    form = UserCreationForm()
    all_users = User.objects.all()
    newuser = User.objects.filter(profile__user_id__isnull=True)
    grouplist = Group.objects.all()
    projectlist = Project.objects.all() 

    context = {'form':form,'all_users':all_users,'newuser':newuser,'grouplist':grouplist,'projectlist':projectlist}
    if request.method =="POST": 
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            print(f'The new user is created')
            return redirect('user')
    return render(request,'accounts/user.html',context)

def employee(request):
    if request.method =="POST": 
        returneduser = request.POST.get('newuser')
        returnedrole = request.POST.get('role')
        returnedgroup = request.POST.get('group_member')
        returnedproject = request.POST.get('project_member')

        ec = Profile(user=User.objects.get(id=returneduser),
                    role=returnedrole,
                    group_member=Group.objects.get(id=returnedgroup),
                    project_member=Project.objects.get(id=returnedproject))
        if ec.check:
            ec.save()
            print(f'The New Employee is with username {returneduser} is Created ')
            return redirect('user')
    return render(request,'accounts/user.html')

def deleteUser(request, pk):
    emp =User.objects.get(id=pk)
    print(emp)
    if request.method =="POST":
        emp.delete()
        return redirect('user')
    return render(request,'accounts/delete.html',{'emp':emp})


def updateUser(request, pk):
    emp = Profile.objects.get(id=pk)
    form = EmployeeCreatiionForm(instance=emp)
    if request.method=="POST":
        form = EmployeeCreatiionForm(request.POST,instance=emp)
        if form.is_valid():

            form.save()
            return redirect('user')
    context={'form':form}
    return render(request,'accounts/update.html',context)



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

