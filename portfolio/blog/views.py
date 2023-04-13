from django.shortcuts import render
from .models import Project,Blog


def blog(request):
    # order_by('-date') сортировка по дате
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/blog.html', {'blogs':blogs})

def home(request):
    projects = Project.objects.all()
    return render(request, 'blog/home.html', {'projects': projects})
