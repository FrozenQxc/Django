from django.shortcuts import render, get_object_or_404
from .models import Project, Blog

def blog(request):
    # Отсортировать блоги по дате в порядке убывания
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/blog.html', {'blogs': blogs})

def home(request):
    # Отсортировать проекты по id в порядке убывания
    projects = Project.objects.all().order_by('-id')
    return render(request, 'blog/home.html', {'projects': projects})

def detail(request, blog_id):
    # Найти сообщение блога по id или вернуть ошибку 404
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
