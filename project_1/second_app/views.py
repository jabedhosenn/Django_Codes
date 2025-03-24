from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def courses(request):
    return HttpResponse("This is second app courses page")

def about(request):
    return HttpResponse("This is second app about page")

def blog(request):
    return HttpResponse("This is second app blog page")

def home(request):
    return HttpResponse("This is second app page")