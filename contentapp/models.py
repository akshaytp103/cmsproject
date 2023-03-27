from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    summary = models.CharField(max_length=200)
    categories = models.CharField(max_length=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contents')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title