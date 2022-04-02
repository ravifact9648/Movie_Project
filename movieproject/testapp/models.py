from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name=models.CharField(max_length=30)
    movie_date=models.DateField()
    movie_rating=models.IntegerField()
    movie_hero_name=models.CharField(max_length=30)
    movie_heroine_name=models.CharField(max_length=30)
