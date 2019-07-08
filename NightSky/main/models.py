from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    body = models.TextField(default='')
    writer = models.TextField(default='')
    pub_date = modles.DateTimeField(default='')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    published_date = models.DateTimeField(
        blank=True, null=True
    )
