from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    Ersteller = models.ForeignKey(User, on_delete=models.CASCADE)
    Lernfeld = models.CharField(max_length=100)
    Beschreibung = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Gebaeudeerstellen(models.Model):
    owner = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    postalcode= models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    lat = models.FloatField(default='0000000')
    lon = models.FloatField(default='0000000')
    
    def __str__(self):
        return self.name
    
    