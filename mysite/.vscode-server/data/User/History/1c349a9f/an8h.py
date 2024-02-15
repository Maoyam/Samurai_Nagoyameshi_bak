from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import RegisteredUser


class RegisteredUser(UserAdmin):
    pass

RegisteredUser = get_user_model()
admin.site.register(RegisteredUser, RegisteredUserAdmin)
