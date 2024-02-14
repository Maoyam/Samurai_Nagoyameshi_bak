from typing import Any
from django.views.generic import TemplateView, ListView
from commondb.models.restaurant import Restaurant

class ShopListView(TemplateView):
    template_name = "general/shop_list.html"
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        # modelで定義した店舗のオブジェクトを取得
        context['restaurants'] = Restaurant.objects.all()

        return context