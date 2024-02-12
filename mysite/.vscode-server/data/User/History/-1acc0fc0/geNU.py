from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100,default="")  
    
    def __str__(self):
        return self.name

class GenreImage(models.Model):   
     image = models.ImageField(upload_to='genre_images/')