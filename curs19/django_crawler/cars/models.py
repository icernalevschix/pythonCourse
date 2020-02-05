from django.db import models

class Car(models.Model):
    price = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
