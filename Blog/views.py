from django.shortcuts import render, redirect, get_object_or_404
from Base.models import User, Verification
from . models import Post, Category, Comment
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  posts = Post.objects.all()

  context = {
    'posts': posts
  }
  return render(request, 'index.html', context)

@login_required(login_url='/account/login/')
def logoutView(request):
  logout(request)
  return redirect('index')

@login_required(login_url='/account/login/')
def createPost(request):
  if request.user.is_complete == False:
    return redirect('complete_reg')
  category = Category.objects.all()
  
  if request.method == 'POST':
    Post.objects.create(
      user = request.user,
      image = request.FILES['image'],
      title = request.POST.get('title'),
      body = request.POST.get('body'),
      category = get_object_or_404(Category, name=request.POST.get('category'))
    )
    messages.info(request, 'Post Created Successfully')
    return redirect('index')

  context = {
    'category':category
  }
  return render(request, 'create_post.html', context)

def View_Post(request, slug):
  post = get_object_or_404(Post, slug=slug)

  context = {
    'post': post
  }
  return render(request, 'view.html', context)

def view_user(request, username):
  user = get_object_or_404(User, username=username)
  # follow, created = Follow.objects.get_or_create(follower=request.user, following=user)
  user_post = user.post_set.all()

  context = {
    'user': user,
    'user_post':user_post
  }
  return render(request, 'profile.html', context)
