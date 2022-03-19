from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=35)
    director = models.CharField(max_length=30)
    length_minutes = models.IntegerField()
    gender = models.CharField(max_length=20)
    
    
class Series(models.Model):
    title = models.CharField(max_length=35)
    director = models.CharField(max_length=30)
    length_minutes = models.IntegerField()
    gender = models.CharField(max_length=20)
    seasons = models.IntegerField()
    
    
class Songs(models.Model):
    title = models.CharField(max_length=35)
    artist = models.CharField(max_length=30)
    length_minutes = models.IntegerField()
    gender = models.CharField(max_length=20)

 