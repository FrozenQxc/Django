from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo
from django.utils import timezone

def home(request):
    return render(request, 'todo/home.html')

# Регистрация пользователя
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
                return redirect('current_todos') 
            else:
                return render(request, 'todo/signup_user.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})
        except IntegrityError:
            # если имя пользователя уже существует, вернуть ошибку
            return render(request, 'todo/signup_user.html', {'form': UserCreationForm(), 'error': 'Имя пользователя уже существует'})
        except KeyError:
            return render(request, 'todo/signup_user.html', {'form': UserCreationForm(), 'error': 'Все поля должны быть заполнены'})

# Вход пользователя в систему
def login_user(request):
    if request.method == 'GET':
        return render(request, 'todo/login_user.html', {'form': AuthenticationForm()})
    else:
        # Аутентификация пользователя
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('current_todos')
        else:
            return render(request, 'todo/login_user.html', {'form': AuthenticationForm(), 'error': 'Имя пользователя или пароль неверны'})

# Выход пользователя из системы
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

# форма которая сохраняет запись пользовтеля 
def create_todo(request):
    if request.method == 'GET':
        return render(request, 'todo/create_todo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('current_todos')
        except ValueError:
            return render(request, 'todo/create_todo.html', {'form': TodoForm(), 'error': 'Переданны не верный данные'})
            

def current_todos(request):
    # фильтрация записией, отображение записей юзера
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'todo/current_todos.html', {'todos': todos})

def view_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/view_todo.html', {'todo': todo, 'form':form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('current_todos')
        except ValueError:
            return render(request, 'todo/view_todo.html', {'todo': todo, 'form':form ,'error': 'Возникла ошибка'})

def complete_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('current_todos')
    
def delete_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.delete()
        return redirect('current_todos')