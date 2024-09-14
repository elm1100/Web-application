from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("Hello world")

def e(request):
    return HttpResponse("Hello e")

def page(request):
    return render(request,"page.html")