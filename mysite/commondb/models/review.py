from django.db import models
from .restaurant import Restaurant


class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    visit_date = models.DateField()
    rating = models.IntegerField(choices=[(1, '1'),(2, '2'),(3, '3'), (4, '4'), (5, '5')])
    comment = models.TextField()
    

class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='review_images/', blank=True, null=True)