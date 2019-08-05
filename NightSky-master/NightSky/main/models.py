from __future__ import unicode_literals
from django.db import models
from decimal import Decimal
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.
class Post(models.Model):
    body=models.TextField(default='')
    #pub_date=models.DateTimeField(auto_now_add=True)
    pub_date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    emotion = models.CharField(max_length=255, blank=False)
    image=models.TextField(default='')
    lng=models.TextField(default='')
    lat=models.TextField(default='')
    distinct=models.TextField(default='')
    #lng = models.DecimalField(max_digits = 8, decimal_places = 3, default=Decimal(0))
    #lat = models.DecimalField(max_digits = 8, decimal_places = 3, default=Decimal(0))
"""   
class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    content=models.TextField(default='')
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
"""

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __str__(self):
        return (self.author.username if self.author else "무명")+ "의 댓글"

class todayemotion(models.Model):
    emotion=models.TextField(default='')
    to=models.TextField(default='')
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE)

