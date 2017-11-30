from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .core import post


@login_required(login_url='/redditauth/authorize')
def home(request):
    return HttpResponse('This is the home page!')


@login_required(login_url='/redditauth/authorize')
def create_post(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        redditpost = form.save()
        post.apply_async((request.user, redditpost), eta=redditpost.time)

    return render(request, 'create-post.html', {'form': form})
