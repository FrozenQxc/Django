from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=250)
    image =  models.ImageField(upload_to='porfolio/images')
    url = models.URLField(blank=True)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()
    date = models.DateField()