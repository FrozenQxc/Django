from django.shortcuts import render
import random

# Создадние функции которая возаращает html
def describing(request):
    return render(request, 'generator/describing.html')

def home(request):
    return render(request, 'generator/home.html')

# Функция возращает запрос генерации пароля
def password(request):
    characters = list('qwertyuiopasdfghjklzxcvbnm')
    # Выбор метода
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('number'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))

    length = int(request.GET.get('length', 10))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
