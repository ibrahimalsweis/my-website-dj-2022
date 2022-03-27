
import email
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



class Comment(models.Model):

 
    name = models.CharField(max_length=100 ,verbose_name='أسم المستخدم ')
    email = models.EmailField(verbose_name='ألبريد ألالكتروني')
    content_comment = models.TextField(max_length=5000,verbose_name='محتوى التعليق ')
    date_comment = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(Post,on_delete=models.CASCADE , related_name='comments')

    def __str__(self):
        return f'تم التعليق بواسطة {self.name} على {self.content_comment}'

    class Meta:
        ordering = ('date_comment',)