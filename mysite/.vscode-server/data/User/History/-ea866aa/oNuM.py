from django.contrib.auth.models import AbstractUser
from django.db import models

class RegisteredUser(AbstractUser):
  # 登録会員向けのモデル
    display_name = models.CharField(max_length=50)
    is_premium_member = models.BooleanField(default=False)
      
    def get_short_name(self):
        """Return the short name for the user."""
        return self.display_name 


class PremiumUser(models.Model):
  # 有料会員向けのモデル
    user = models.OneToOneField(RegisteredUser, on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=50)
