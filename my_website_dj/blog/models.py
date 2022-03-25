from operator import mod
from turtle import update
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Post(models.Model):
    content_post = models.TextField(max_length=10000)
    date_post = models.DateTimeField(default=timezone.now)
    update_post = models.DateTimeField(auto_now=True)
    auth = models.ForeignKey(User,on_delete=models.CASCADE )

    def __str__(self):
        return str(self.content_post)

    class Meta:
        ordering = ('-date_post', )