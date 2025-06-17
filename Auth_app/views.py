from django.shortcuts import render, HttpResponseRedirect
from .forms import CreateNewUser
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy


# Create your views here.
def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            registered = True
            pass
    return render(request, 'auth_app/sign_up.html',context={'form':form, 'registered':registered})