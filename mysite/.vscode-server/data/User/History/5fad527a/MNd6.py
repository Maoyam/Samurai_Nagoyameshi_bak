from typing import Any
from django.views.generic import TemplateView
from commondb.models.review import Review
from commondb.models.restaurant import Restaurant


class ShopReviewView(TemplateView):
    template_name = "general/shop_detail.html"
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
         # URLから店舗のIDを取得
        restaurant_id = self.kwargs.get('pk')
        # 対象の店舗に関連するレビューを取得
        context['reviews'] = Review.objects.filter(restaurant_id=restaurant_id)
        # 対象の店舗情報を取得してコンテキストに追加
        context['restaurant'] = Restaurant.objects.get(pk=restaurant_id)
        return context