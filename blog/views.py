from django.shortcuts import render
from .models import Post
from django.utils import timezone

def mostrar(request):
     posts = Post.objects.all()
     return render(request , 'blog/list_posts.html', {'posts':posts})