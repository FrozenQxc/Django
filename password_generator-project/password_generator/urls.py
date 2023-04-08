from django.urls import path
from generator.views import home, password, describing


# Создание маршрутов url
urlpatterns = [
    path('', home, name='home'),
    path('describing/', describing, name='describing'),
    path('password/', password, name='password'),
]

