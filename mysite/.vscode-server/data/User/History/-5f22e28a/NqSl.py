from django.shortcuts import render, redirect
from django.views import View
from commondb.models.user import User
from django.views.generic.edit import UpdateView

class UserEditView(UpdateView):
    model = User
    fields ='__all__'
    template_name = 'account_edit'
    