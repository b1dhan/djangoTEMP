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

def pfp_view(request, id):
    return HttpResponse(f'This is profile view {id}')

def html_view(request):
    posts = Posts.objects.all()
    return render(request, 'firstapp/index.html', {"posts": posts})

def intro_view(request):
    message='I am Robot'
    return render(request, 'firstapp/intro.html', {"message":message})

@login_required
def create_post(request):
    # CRUD operation
    if request.method=="POST":
        post=CreateBlogPostForm(request.POST)
        if post.is_valid():
            new_post = post.save(commit=False)   
            new_post.created_by = request.user    
            new_post.save()
            messages.success(request, "Post created successfully.")
            return redirect('html_view')
        else:
            messages.error(request, "Please fix the errors below.")
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
from django.contrib import messages
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            user.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! Your account was created.")
            return redirect('html_view')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})

from django.contrib.auth import login,authenticate,logout      
def login_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('html_view')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login_view')
    return render(request, 'login.html')

def logout_view(request):
    if request.method=="POST":
        logout(request)
        messages.info(request, "You have been logged out.")
        return redirect("html_view")

from django.core.exceptions import PermissionDenied
@login_required
def edit_post(request, id):
    post = get_object_or_404(Posts, pk=id)
    if post.created_by != request.user:
        raise PermissionDenied
    # after submission of form
    if request.method=="POST":
        form=CreateBlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully.")
            return redirect('post_detail', post_id=id)
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form=CreateBlogPostForm(instance=post)
    return render(request, "firstapp/edit_post.html", {
            "post":post,
            "form":form
        })

# protected features need auth user (logged in)
@login_required
def delete_post(request, id):
    post = get_object_or_404(Posts, pk=id)

    if post.created_by != request.user:
        raise PermissionDenied

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted.")
        return redirect('html_view')
    return render(request, "firstapp/deletepostconfirm.html", {"post": post})

# added search feature using GET, q parameter, __icontains condition
def search(request):
    q = request.GET.get('q', '').strip()
    posts = Posts.objects.all()
    if q:
        posts = posts.filter(title__icontains=q)
    return render(request, 'firstapp/index.html', {"posts": posts, "q": q})

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was updated successfully.")
            return redirect('password_change_done')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "firstapp/change_password.html", {"form": form})


@login_required
def change_password_done(request):
    return render(request, "firstapp/change_password_done.html")

@login_required
def profile_view(request):
    return render(request, "profile.html", {"user":request.user})