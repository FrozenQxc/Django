from django.contrib import admin
# импорт моделей для админки 
from .models import Project,Blog

admin.site.register(Project)
admin.site.register(Blog)
