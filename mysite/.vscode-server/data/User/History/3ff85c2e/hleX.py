from django.db import models
from .restaurant import Restaurant

class Review(models.Model):
    name = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    visit_date = models.DateField(input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'type': 'date'}),)
    rating = models.IntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')])
    comment = models.TextField()
    image1 = models.ImageField(upload_to='review_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='review_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='review_images/', null=True, blank=True)

    
    