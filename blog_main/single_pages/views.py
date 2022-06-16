from django.shortcuts import render

# Create your views here.
from blog.models import Post
# 빨간 줄이 맞는거

def landing(request):
    return render(request, 'single_pages/landing.html',{
        'recent_posts': Post.objects.order_by('-pk')[:3],
    })

def about_me(request):
    return render(request, 'single_pages/about_me.html')