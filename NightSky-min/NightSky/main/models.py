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

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(default='')
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE, default='')
    writer = models.CharField(max_length=255, default='', blank=True)
    created_at = models.DateTimeField(default = timezone.now)

class todayemotion(models.Model):
    emotion=models.TextField(default='')
    to=models.TextField(default='')
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE)

