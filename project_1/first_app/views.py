from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def courses(request):
    return HttpResponse("This is courses page")

def about(request):
    return HttpResponse("This is about page")

def blog(request):
    return HttpResponse("This is blog page")

def home(request):
    return HttpResponse("This is first app page")