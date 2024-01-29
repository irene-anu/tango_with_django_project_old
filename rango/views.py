from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):   # here the request is a HttpRequest object
    # each view must return a HttpResponse object
    return HttpResponse("Rango says hey there partner!")