from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.RESTRICT)
    title = models.CharField(max_length=128)
    content = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    # images = models.ImageField ## TODO: static files configuration