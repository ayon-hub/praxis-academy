from django.db import models

# Create your models here.
class Pegawai(models.Model):
    nama = models.TextField(default='')
    contact = models.IntegerField(default='')