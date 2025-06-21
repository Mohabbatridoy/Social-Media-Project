from .forms import CreateNewUser , EditProfile
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from app_post.forms import PostForm


#create your views here.
def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('auth_app:login'))

    return render(request, 'auth_app/sign_up.html', context={'title':'sign_up.instagram', 'form':form, 'registered':registered})

def Log_in(request):
    form = AuthenticationForm()
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('app_post:home'))

    return render(request, 'auth_app/log_in.html', context={'title':'Login', 'form':form})

@login_required
def Edit_Profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)
    if request.method=="POST":
        form = EditProfile(request.POST,request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('auth_app:profile'))

    return render(request, 'auth_app/profile.html', context={'form':form, 'title':'edit Profile.social'})

@login_required
def LogOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('auth_app:login'))

@login_required
def Profile(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'auth_app/user.html', context={'title':'Profile', 'form':form })