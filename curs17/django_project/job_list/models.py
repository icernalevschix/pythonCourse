from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta

def expire_date(offset):
    return timezone.now() + timedelta(days=offset)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_expire = models.DateTimeField(default=expire_date(30))
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title