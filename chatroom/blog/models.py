from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):

    name = models.CharField(max_length=40,unique=True)
    password = models.CharField(max_length=40)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('UserProfile')

    def __str__(self):
        return self.comment
