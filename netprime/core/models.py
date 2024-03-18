from django.db import models
import uuid
from django.conf import settings
# Create your models here.
class Movie(models.Model):

    GENRE_CHOICES = (
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('sci-fi', 'Sci-Fi'),
        ('thriller', 'Thriller'),
        ('western', 'Western'),
    )

    uu_id = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES)
    length = models.PositiveIntegerField()
    image_card= models.ImageField(upload_to='movie_images/')
    image_cover = models.ImageField(upload_to='movie_images/')
    video = models.FileField(upload_to='movie_videos/')
    movie_views= models.PositiveIntegerField(default=0)

    
    def __str__(self):
        return self.title
    

class MovieList (models.Model):
    owner_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

