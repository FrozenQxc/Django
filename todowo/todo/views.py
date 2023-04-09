from django.shortcuts import render
# Импорт формы для регистрации
from django.contrib.auth.forms import UserCreationForm

def singnupuser(request):
    return render(request, 'todo/singnupuser.html', {'form': UserCreationForm()}) 

def home(request):
    return render(request, 'todo/home.html')