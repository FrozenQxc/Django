from django.shortcuts import render
# Ипортирование проекта 
from .models import Project

def home(request):
    # получение данных из базы данных 
    projects =  Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})