from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    # return HttpResponse("This is first app home page")
    return render(request, 'first_app/home.html')