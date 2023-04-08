from django.db import models
class Blog(models.Model):
    title = models.CharField(max_length=200)
    # des = models.TextField()
    date = models.DateField()
