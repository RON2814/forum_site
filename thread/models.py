from django.db import models
from forum.models import Forum
from django.contrib.auth.models import User

# Create your models here.


class Thread(models.Model):
    forum = models.ForeignKey(
        Forum, related_name='threads', on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} - {self.created_by}"
