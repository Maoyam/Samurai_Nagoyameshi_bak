from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_paid_member = models.BooleanField(verbose_name='有料会員', default=False)
    is_manage_member = models.BooleanField(verbose_name='管理者', default=False)
    display_name = models.CharField(verbose_name='ユーザー名' max_length=10, blank=False, null=False)
    
    def __str__(self):
        return self.display_name
    
    class Meta:
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー一覧'