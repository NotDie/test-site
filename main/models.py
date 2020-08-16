from django.db import models
from tinymce.models import HTMLField


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = HTMLField()
    image = models.ImageField(upload_to = 'images/')
    time = models.TimeField(auto_now=False, auto_now_add=True, blank=True)
