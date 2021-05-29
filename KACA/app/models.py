from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, default=None)
    introduction = models.CharField(max_length=200, default=None)
    content = models.TextField(default=None)
    target = models.CharField(max_length=200, default=None)
    logo = models.ImageField(blank=True)
    apply_start = models.DateTimeField(null=True, blank=True)
    apply_end = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True, default=None)
    category = models.CharField(max_length=10, default=None)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', default=None)
    content = models.TextField(default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True, default=None)

class Lecture(models.Model):
    title = models.CharField(max_length=200, default=None)
    introduction = models.CharField(max_length=200)
    content = models.TextField(default=None)
    thumbnail = models.ImageField(blank=True)
    price = models.CharField(max_length=200, default=None)
    construct = models.CharField(max_length=200, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lectures', null=True, default=None)
    category = models.CharField(max_length=10, default=None)

    def __str__(self):
        return self.title