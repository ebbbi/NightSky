from django.db import models

# Create your models here.
<<<<<<< Updated upstream
=======
class Post(models.Model):
    body = models.TextField(default='')
    writer = models.TextField(default='')
    pub_date = models.DateTimeField(default='')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    published_date = models.DateTimeField(
        blank=True, null=True
    )
    

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    content=models.TextField(default='')
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
>>>>>>> Stashed changes
