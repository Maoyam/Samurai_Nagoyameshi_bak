from django.db import models
from .restaurant import Restaurant

class Booking(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name