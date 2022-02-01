from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to task app")
def detail(request):
    return HttpResponse("Welcome to detail of task app")
def about(request):
    return HttpResponse("Welcome to about of task app")
