from typing import Any
from django.views.generic import TemplateView

class ShopDetailView(TemplateView):
    template_name = "general/shop_detail.html"
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        # modelで定義した店舗のオブジェクトを取得
        context['restaurants'] = Area.objects.all()

        return context