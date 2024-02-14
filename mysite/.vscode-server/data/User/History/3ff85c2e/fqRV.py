from django.db import models
from models.restaurant import Restaurant

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)