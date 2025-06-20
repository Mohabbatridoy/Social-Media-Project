from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from Auth_app.models import UserProfile

# Create your views here.

@login_required
def home(request):
    user_info = UserProfile

    return render(request, 'app_post/home.html', context={'title':'Homepage', 'user':user_info})