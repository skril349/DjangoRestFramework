from django.db import models

# Create your models here.

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('posts.Post', related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='comments', on_delete=models.SET_NULL, null=True, blank=True)
    