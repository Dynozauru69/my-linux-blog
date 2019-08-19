from django.shortcuts import render
from .models import Post
from django.utils import timezone

def mostrar(request):
     return render(request , 'blog/list_posts.html')