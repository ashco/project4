from django.shortcuts import render
from django.http import HttpResponse

from django.utils import timezone

# MODELS
from .models import Post



def index(request):
    # return HttpResponse('Hello from posts')

    # get last 10 posts, (not including those set to be published in the future)
    # get_queryset = Post.objects.all()[:10] 
    get_queryset = Post.objects.filter(
        created_at__lte=timezone.now()
    ).order_by('-created_at')[:10]

    context = {
        'title': 'Latest Posts',
        'posts': get_queryset
    }
    
    return render(request, 'posts/index.html', context)

def details(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }
    
    return render(request, 'posts/details.html', context)