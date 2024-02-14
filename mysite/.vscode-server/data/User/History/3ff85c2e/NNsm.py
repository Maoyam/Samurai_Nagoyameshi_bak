from django.db import models
from .restaurant import Restaurant

class Review(models.Model):
    restaurant_name = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    visit_date = models.DateField()
    rating = models.IntegerField()
    images = models.ImageField(upload_to='review_images/', blank=True, null=True)
    comment = models.TextField()
    