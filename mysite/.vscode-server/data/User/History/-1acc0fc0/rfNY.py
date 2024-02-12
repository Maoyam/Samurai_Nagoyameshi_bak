from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class GenreImage(models.Model):
    genre = models.OneToOneField(Genre, on_delete=models.CASCADE)
    Img = models.ImageField(upload_to='genre_images/')