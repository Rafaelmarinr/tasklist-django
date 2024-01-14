from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Proyect, Task
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return HttpResponse('<h1>Index Page</h1>')

def hello(request, username):
    return HttpResponse('<h1>Hello %s</h1>' % username)

def about(request):
    return HttpResponse('<h1>About</h1>')

def projects(request):
    projects = list(Proyect.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, title):
    task = Task.objects.get(title=title)
    return HttpResponse('Tasks %s' % task.title)
