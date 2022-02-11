from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.




def addincident(request):
    return render(request,'incident/addincident.html')

from django.shortcuts import render
from .forms import IncidentForm
# Create your views here.


def add_incident(request):
    form = IncidentForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = IncidentForm()
    return render(request,"incident/add-incident.html",{"form":form})
    # return render(request,"incident/incident.html",{"form":form})



