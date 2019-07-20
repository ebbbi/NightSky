from __future__ import unicode_literals
from django.db import models
from decimal import Decimal
# Create your models here.
class Post(models.Model):
    body=models.TextField(default='')
    pub_date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    emotion = models.CharField(max_length=255, blank=False)
    lng = models.DecimalField(max_digits = 8, decimal_places = 3, default=Decimal(0))
    lat = models.DecimalField(max_digits = 8, decimal_places = 3, default=Decimal(0))

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    content=models.TextField(default='')
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
