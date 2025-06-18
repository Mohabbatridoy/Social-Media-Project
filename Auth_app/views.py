from .forms import CreateNewUser
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm

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
                pass

    return render(request, 'auth_app/log_in.html', context={'title':'Login', 'form':form})