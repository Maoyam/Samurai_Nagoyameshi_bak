from django.db import models
from .restaurant import Restaurant
from .user import User

class Booking(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name="店舗ID")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ユーザーID")
    booking_date = models.DateField(verbose_name="予約日")
    booking_time = models.TimeField(verbose_name="予約時間")
    numbers_of_ppl = models.IntegerField(default=0, verbose_name="予約人数")
    create_date = models.TimeField(auto_now_add=True, verbose_name="作成日時")
    
    def __str__(self):
        return self.name