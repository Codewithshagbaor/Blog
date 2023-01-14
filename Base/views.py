from django.shortcuts import render, redirect, get_object_or_404
from Base.models import User, Verification
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import uuid
# Create your views here.

def signUpView(request):
  if request.user.is_authenticated:
    messages.info(request,'Logged in Already')
    return redirect('index')

  if request.method == 'POST':
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')

    if password == password2:
      if User.objects.filter(username=username).exists():
        messages.info(request, "Username Taken")
        return redirect('signup')
      elif User.objects.filter(email=email):
        messages.info(request, "Email Already Exists")
        return redirect('signup')
      else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save();
        login(request, user)
        messages.info(request, 'Successfully create an Account Complete Your Registration')
        return redirect('complete_reg')
    else:
      messages.info(request, "Password not Thesame")
      return redirect('signup')
  return render(request, "signup.html")


def loginView(request):
  if request.user.is_authenticated:
    messages.info(request,'Logged in Already')
    return redirect('index')

  if request.method == 'POST':
    username=request.POST.get('username')
    password=request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    
    if user is not None:
      login(request, user)
      messages.info(request, 'Successfully Logged in')
      return redirect('index')
    else:
      messages.error(request, 'Invalid Details')

  return render(request, 'login.html')

@login_required(login_url='/account/login/')
def complete_reg(request):
  if request.user.is_complete:
    return redirect('index')

  if request.method == 'POST':
    user = request.user
    
    bio = request.POST.get('bio')
    location = request.POST.get('location')
    name = request.POST.get('name')
    profile_img=request.FILES['profile_img']

    user.name = name
    user.bio = bio
    user.location = location
    user.profile_img = profile_img
    user.is_complete = True
    user.save();
    return redirect('index')
  return render(request, "complete_reg.html")

