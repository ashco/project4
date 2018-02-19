from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def index(request):
    # return HttpResponse('Hello from posts')

    all_posts = Post.objects.all()[:10] # get first 10 posts

    context = {
        'title': 'Latest Posts',
        'posts': all_posts
    }

    # return render(request, 'posts/index.html', {
    #     'title': 'Latest Posts'
    # })
    
    return render(request, 'posts/index.html', context)

def details(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }
    
    return render(request, 'posts/details.html', context)