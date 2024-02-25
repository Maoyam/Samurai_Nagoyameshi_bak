from django.core.exceptions import ValidationError
from datetime import date, timedelta
from django.db import models
from .restaurant import Restaurant
from .user import User

def future_date_validator(value):
    if value <= date.today():
        raise ValidationError('予約日は翌日以降を選択してください。')

class Booking(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name="店舗ID")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ユーザーID")
    booking_date = models.DateField(verbose_name="予約日", validators=[future_date_validator])
    booking_time = models.TimeField(verbose_name="予約時間")
    numbers_of_ppl = models.IntegerField(default=0, verbose_name="予約人数")
    create_date = models.TimeField(auto_now_add=True, verbose_name="作成日時")
    
    def __str__(self):
        return self.name