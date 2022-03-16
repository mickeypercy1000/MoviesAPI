from django.db import models

# Create your models here.

import datetime
YEAR_OPTIONS = []
for date_range in range(1960, (datetime.datetime.now().year+1)):
    YEAR_OPTIONS.append((date_range,date_range))
    
movie_genres = [
    ('Action', 'action'),
    ('Comedy', 'comedy'),
    ('Drama', 'drama'),
    ('Horror', 'horror'),
    ('Thriller', 'thriller'),
    ('Sci-Fi', 'sci-fi'),
    ('Romance', 'romance'),
    ('Western', 'western'),
    ('Action', 'action'),
    ('Crime', 'crime'),
    ('Adventure', 'adventure'),
    ('Musical', 'musical'),
    ('Animation', 'animation'),
    ('Fantasy', 'fantasy'),
    ('Documentary', 'documentary')
]

movie_status = [
    ('Released', 'released'),
    ('Upcoming', 'upcoming')
]
class MoviesAPI(models.Model):

    id                      = models.CharField(primary_key=True, max_length=50, unique=True)
    movie_title             = models.CharField(max_length=255, unique=True)
    movie_description       = models.TextField()
    genre                   = models.CharField(choices = movie_genres, max_length=20, default='Action')
    movie_year              = models.IntegerField(('year'), choices=YEAR_OPTIONS, default=datetime.datetime.now().year) 
    status                  = models.CharField(choices = movie_status, max_length=20) 
    date_created            = models.DateTimeField(auto_now_add=True, null=True, blank = True)
    date_updated            = models.DateTimeField(auto_now=True, null=True, blank = True)

