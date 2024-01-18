from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Proyect, Task
from .forms import CreateNewTask, CreateNewProject
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
    return render(request, 'projects/projects.html', {'projects': projects})

def tasks(request):
    #task = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'GET':
        #show interface
        return render(request, 'tasks/create_task.html',{
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], proyect_id=2)
        return redirect('/tasks/')
        
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        project = Proyect.objects.create(name = request.POST['name'])
        print(project)
        render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
        return redirect('/projects')