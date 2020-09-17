from django.db import models

class Bahan(models.Model):
    nama = models.TextField(default='')
    stok = models.IntegerField(default='')