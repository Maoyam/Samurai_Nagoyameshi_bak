from typing import Any
from commondb.models.booking import Booking
from commondb.models.review import Review
from commondb.models.favorite import Favorite
from django.views.generic import TemplateView

class MypageView(TemplateView):
    template_name = "general/mypage.html"
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        
        # Favoriteオブジェクトを取得し、関連するRestaurantオブジェクトも同時に取得する
        favorites_with_restaurant = Favorite.objects.select_related('restaurant').all()
        # modelで定義した予約のオブジェクトを取得
        context['bookings'] = Booking.objects.all()
        # modelで定義したレビューのオブジェクトを取得
        context['reviews'] = Review.objects.all()
        # お気に入りのオブジェクトとそれに関連するRestaurantオブジェクトをコンテキストに追加
        context['favorites'] = favorites_with_restaurant

        return context