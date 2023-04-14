from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

def home(request):
    return render(request, 'todo/home.html')

# шаблон для регистрации пользователя
def signup_user(request):
    if request.method == 'GET':

        return render(request, 'todo/signup_user.html', {'form': UserCreationForm()})
    else:
        try:
            if request.POST['password1'] == request.POST['password2']:
                # если пароли совпадают, создать нового пользователя
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos') 
            else:
                return render(request, 'todo/signup_user.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})
        except IntegrityError:
            # если имя пользователя уже существует, вернуть ошибку
            return render(request, 'todo/signup_user.html', {'form': UserCreationForm(), 'error': 'Имя пользователя уже существует'})
        except KeyError:
            return render(request, 'todo/signup_user.html', {'form': UserCreationForm(), 'error': 'Все поля должны быть заполнены'})

# Шаблон для входа пользователя
def login_user(request):
    if request.method == 'GET':
        return render(request, 'todo/login_user.html', {'form': AuthenticationForm()})
    else:
        # Аутентификация пользователя
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'todo/login_user.html', {'form': AuthenticationForm(), 'error': 'Имя пользователя или пароль неверны'})

# Выход пользователя из системы
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    

        

def currenttodos(request):
    return render(request, 'todo/currenttodos.html')
