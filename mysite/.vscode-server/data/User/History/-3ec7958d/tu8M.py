from typing import Any
from django.views.generic import DetailView
from commondb.models.restaurant import Restaurant
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from commondb.models.user import User

class ShopDetailView(LoginRequiredMixin, DetailView):
    model = Restaurant
    #詳細ページのテンプレート名
    template_name = "general/shop_detail.html"
    # テンプレート内でのオブジェクトの名前
    context_object_name = 'restaurant'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            if self. request.user.is_paid_member:
                context['user_type'] = 'is_paid'
            else:
                context['user_type'] = 'member'
        else:
            context['user_type'] = 'no_member'
        return context
