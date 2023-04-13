from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=250)
    image = models.ImageField(upload_to='porfolio/images')
    url = models.URLField(blank=True)

    # Возращает заголовок(title) что бы в админке было видно
    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
