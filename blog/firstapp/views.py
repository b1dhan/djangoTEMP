from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# two ways: class based, function based
# function based haru:
def first_view(request):
    return HttpResponse("Hello Friend this is first view")

def profile_view(request, id):
    return HttpResponse(f'This is profile view {id}')

def html_view(request):
    message='Welcome Home!'
    return render(request, 'firstapp/index.html', {"message":message})

def intro_view(request):
    message='I am Robot'
    return render(request, 'firstapp/intro.html', {"message":message})