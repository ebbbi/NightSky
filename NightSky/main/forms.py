from django import forms
from .models import Post, Comment

class PostForm(forms.modelForm):
    class Meta:
        model = Post
        fields=['body','writer','author','pub_date',]


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content',]
    