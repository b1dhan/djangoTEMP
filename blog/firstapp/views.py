from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts
from .forms import CreateBlogPostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# two ways: class based, function based
# function based haru:
def first_view(request):
    return HttpResponse("Hello Friend this is first view")

def profile_view(request, id):
    return HttpResponse(f'This is profile view {id}')

# added search feature using GET, q parameter, __icontains condition
def html_view(request):
    q = request.GET.get('q', '').strip()

    posts = Posts.objects.all()
    if q:
        posts = posts.filter(title__icontains=q)

    return render(request, 'firstapp/index.html', {"posts": posts, "q": q})

def intro_view(request):
    message='I am Robot'
    return render(request, 'firstapp/intro.html', {"message":message})

@login_required
def create_post(request):
    # CRUD operation
    if request.method=="POST":
        post=CreateBlogPostForm(request.POST)
        if post.is_valid():
            new_post = post.save(commit=False)   # capture the returned model instance
            new_post.author = request.user       # set attribute, not dict key
            new_post.save()
        return redirect('html_view')
    else:
        post=CreateBlogPostForm()
    return render(request, "firstapp/createpost.html",{"post":post})

def get_post_view(request):
    posts=Posts.objects.all()
    return render(request, "firstapp/all_post.html", {"posts":posts})

from django.shortcuts import get_object_or_404
def post_detail_view(request, post_id):
    post=get_object_or_404(Posts, id=post_id)
    return render(request, "firstapp/post_detail.html", {"post":post})

from .forms import SignUpForm
from django.contrib.auth.models import User
def signup_view(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            user.save()
            login(request,user)
            return redirect('html_view')    
    else:   
            form=SignUpForm()
    return render(request, "signup.html", {"form":form})        

from django.contrib.auth import login,authenticate,logout      
def login_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user:
            login(request, user)
        return redirect('html_view')
    return render(request, 'login.html')

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect("html_view")

@login_required
def edit_post(request, id):
    post = get_object_or_404(Posts, pk=id)
    # after submission of form
    if request.method=="POST":
        form=CreateBlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=id)
    else:
        form=CreateBlogPostForm(instance=post)
    return render(request, "firstapp/edit_post.html", {
            "post":post,
            "form":form
        })

