from django.contrib import admin
from testapp.models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['movie_name','movie_date','movie_rating','movie_hero_name','movie_heroine_name']


admin.site.register(Movie,MovieAdmin)
