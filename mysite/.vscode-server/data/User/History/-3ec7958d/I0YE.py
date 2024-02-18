from typing import Any
from django.views.generic import DetailView
from commondb.models.restaurant import Restaurant
from django.contrib.auth.mixins import LoginRequiredMixin

class ShopDetailView(LoginRequiredMixin, DetailView):
    model = Restaurant
    #詳細ページのテンプレート名
    template_name = "general/shop_detail.html"
    # テンプレート内でのオブジェクトの名前
    context_object_name = 'restaurant'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_paid'] = self.request.user.is_paid_member
