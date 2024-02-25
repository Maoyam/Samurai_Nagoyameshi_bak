from django.db import models
from .restaurant import Restaurant
from .user import User

class Booking(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name="店舗ID")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ユーザーID")
    booking_date = models.TimeField()
    numbers_of_ppl = models.IntegerField(initial=0)
    booked_date = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name