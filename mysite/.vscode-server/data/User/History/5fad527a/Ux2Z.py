from typing import Any
from django.views.generic import TemplateView
from commondb.models.review import Review

class ShopReviewView(TemplateView):
    template_name = "general/shop_detail.html"
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        # modelで定義したレビューのオブジェクトを取得
        context['review'] = Review.objects.all()
        return context