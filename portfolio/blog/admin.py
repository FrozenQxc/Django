from django.contrib import admin
# импорт моделей для админки 
from .models import Project

admin.site.register(Project)