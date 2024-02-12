from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100,default="")
    image = models.ImageField(upload_to='static/general/images/')
    
    def __str__(self):
        return self.name