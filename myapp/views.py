from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyect, Task

# Create your views here.

def index(request):
    title = 'Django Curse'
    return render(request, 'index.html', {'title': title})

def about(request):
    username = 'Rafael'
    return render(request, 'about.html', {'username': username})

def hello(request, username):
    return HttpResponse('<h1>Hello %s</h1>' % username)

def projects(request):
    # projects = list(Proyect.objects.values())
    projects = Proyect.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def tasks(request):
    #task = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})
