from typing import Any
from django.views.generic import TemplateView
from ..models.restaurant import Restaurant

class ShopDetailView(DetailView):
    model = Restaurant
    #詳細ページのテンプレート名
    template_name = "general/shop_detail.html"
    # テンプレート内でのオブジェクトの名前
    context_object_name = 'restaurant'
