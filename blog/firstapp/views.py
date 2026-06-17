from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts
from .forms import CreateBlogPostForm

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

def create_post(request):
    # CRUD operation
    if request.method=='POST':
        post=CreateBlogPostForm(request.POST)
        if post.is_valid():
            post.save()
            return redirect('html_view')
    else:
        post=CreateBlogPostForm()

    return render(request, "firstapp/createpost.html",{"post":post})
