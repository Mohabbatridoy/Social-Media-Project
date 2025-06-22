from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from Auth_app.models import UserProfile
from django.contrib.auth.models import User

# Create your views here.

@login_required
def home(request):
    if request.method == "GET":
        search = request.GET.get('search', '')
        result = User.objects.filter(username__icontains=search)
    return render(request, 'app_post/home.html', context={'title':'Homepage', 'search':search, 'result':result})