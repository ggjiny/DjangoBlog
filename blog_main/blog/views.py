from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(request, 'blog/post_list.html',{
#         'posts': posts,
#     })


# def single_post_page(request, pk): #하나만 뽑아오기
#     post = Post.objects.get(pk = pk)
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post': post,
#         }
#     )


class PostList(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post
