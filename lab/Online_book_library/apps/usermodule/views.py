from django.shortcuts import render
from django.http import HttpResponse

def index(request, val1 = 0):
    return HttpResponse("hello from users")
