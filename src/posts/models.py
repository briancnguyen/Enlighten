from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    title = models.CharField(max_length=100)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
