from django.shortcuts import render

# Create your views here.
def home(request):
    d = {'author' : 'Rahim', 'age' : 20, 'lst' : [1,2,3], 'courses': [
        {
            'id' : 1,
            'name': 'Python',
            'fee': 5000
        },
        {
            'id' : 2,
            'name': 'Django',
            'fee': 4500
        },
        {
            'id' : 3,
            'name': 'PHP',
            'fee': 3500
        }
    ]}
    return render(request, 'first_app/home.html', d)