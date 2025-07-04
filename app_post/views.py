from django.urls import reverse
from django.shortcuts import HttpResponse , HttpResponseRedirect, render
from django.contrib.auth.decorators import login_required
from Auth_app.models import UserProfile
from django.contrib.auth.models import User
from Auth_app.models import UserProfile, Follow
from django.contrib.auth.models import User
from .models import Post, Like, comment
from .forms import commentForm

# Create your views here.

@login_required
def home(request):
    following_list = Follow.objects.filter(follower=request.user)
    posts = Post.objects.filter(author__in=following_list.values_list('following'))
    liked_post = Like.objects.filter(user=request.user)
    liked_post_list = liked_post.values_list('post', flat=True)

    followed = Follow.objects.filter(follower=request.user)

    print(liked_post)
    if request.method == "GET":
        search = request.GET.get('search', '')
        result = User.objects.filter(username__icontains=search)
    return render(request, 'app_post/home.html', context={'title':'Homepage', 'search':search, 'result':result, 'posts':posts, 'liked_post_list':liked_post_list, 'followed':followed})

@login_required
def Liked(request, pk):
    post = Post.objects.get(pk = pk)
    already_liked = Like.objects.filter(post=post, user=request.user)
    if not already_liked:
        liked_post = Like(post=post, user=request.user)
        liked_post.save()

    return HttpResponseRedirect(reverse('home'))

@login_required
def Unliked(request, pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post, user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('home'))


@login_required
def Comment(request, pk):
    form = commentForm()

    return render(request, 'app_post/home.html', context={'form':form,})