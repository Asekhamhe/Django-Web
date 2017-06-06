from django.shortcuts import render

# Create your views here.
"""
def index(request):
    # this is your new view
    return render(request, 'index.html')
"""
def index(request):
    # defining the variable
    number = 6
    name = "onaulogho lawrence"
    # passing the variable to the view
    return render(request, 'index.html', {
        'number': number,
        'name': name,
    })
