from django.shortcuts import render 
from .models import Blog

def all_blogs(request):
    # сортировка по дате
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})