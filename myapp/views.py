from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Index Page</h1>')

def hello(request, username):
    return HttpResponse('<h1>Hello %s</h1>' % username)

def about(request):
    return HttpResponse('<h1>About</h1>')

def projects(request):
    return HttpResponse('<h1>Projects</h1>')

def tasks(request):
    return HttpResponse('<h1>Tasks</h1>')
