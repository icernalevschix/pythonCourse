from django.db import models

class FancyCat(models.Model):
    date_added = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, default='')

    class Meta:
        ordering = ('date_added', )


class FluffyTiger(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    color = models.CharField(max_length=32)
    rare = models.BooleanField(default=True)