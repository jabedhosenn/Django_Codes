from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def courses(request):
    return HttpResponse("This is first app courses page")

def about(request):
    return HttpResponse("This is app about page")

def blog(request):
    return HttpResponse("This is app blog page")

def home(request):
    return HttpResponse("This is first app page")