from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'navigation/about.html')

def services(request):
    return render(request, 'navigation/services.html')

def contact(request):
    return render(request, 'navigation/contact.html')