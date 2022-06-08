from cgitb import text
from codecs import namereplace_errors
from django.shortcuts import render
from django.template import loader
from .models import *
# Create your views here.
from django.http import HttpResponse
def home(request,name):
    cont={
        'firstname':['vijay','shashi','teja sai','sai teja']
    }
    
    ls=Todolist.objects.get(name=name)
    # tS=Items.objects.get()
    
    return HttpResponse("<h1>%s </h1>"%ls.name)
def index(request):
    # template=loader.get_template('index.html').render(request)
    return HttpResponse(render(request,"base.html"))
