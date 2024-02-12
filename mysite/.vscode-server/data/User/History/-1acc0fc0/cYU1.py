from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100,default="")
    img = models.ImageField(blank=True, default=None)
    
    def __str__(self):
        return self.name