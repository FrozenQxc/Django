from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    datecomleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    # Специальный ключ для пользовтеля, что бы отображалось его записи!
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    