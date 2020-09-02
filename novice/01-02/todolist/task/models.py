from django.db import models

# Create your models here.
class Task(models.Model):
    menu = models.TextField(default='')
    harga = models.TextField(default='')