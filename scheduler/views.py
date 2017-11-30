from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PostForm


@login_required(login_url='/redditauth/authorize')
def home(request):
    return

@login_required(login_url='/redditauth/authorize')
def create_post(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()

    return render(request, 'create-post.html', {'form': form})
