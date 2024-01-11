from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

tasks=[]
# Create your views here.

class NewTaskForm(forms.Form):
    task= forms.CharField(label="New Task")
    
now=datetime.datetime.today()
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request,"tasks/index.html",{
        "tasks":request.session["tasks"],
        "time":now
    })

def add(request):
    if request.method =="POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task.capitalize()]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request,"tasks/add.html",{
                "form": form
            })
    return render(request,"tasks/add.html",{
        "form":NewTaskForm()
    })
