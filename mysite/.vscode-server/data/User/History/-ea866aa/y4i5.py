from django.contrib.auth.models import AbstractUser
from django.db import models

class RegisteredUser(AbstractUser):
  # 登録会員向けのモデル
    is_premium_member = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username    

  
class PremiumUser(models.Model):
  # 有料会員向けのモデル
    user = models.OneToOneField(RegisteredUser, on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=50)
