from datetime import timezone, datetime
from django.db import models
from django.utils import timezone


class Menu(models.Model):
    names = models.CharField(max_length=50)
    names_info = models.CharField(max_length=50)

    def __str__(self):
        return self.names


class News(models.Model):
    title_news = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_pulished = models.BooleanField(default=True)

    def __str__(self):
        return self.title_news


class Photos(models.Model):
    title = models.CharField(max_length=255)
    photos = models.ImageField(upload_to="photo/%Y/%m/%d")

    def __str__(self):
        return self.title
