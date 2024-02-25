from typing import Any
from commondb.models.booking import Booking
from commondb.models.review import Review
from commondb.models.favorite import Favorite
from django.views.generic import TemplateView

class MypageView(TemplateView):
    template_name = "general/mypage.html"
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        # modelで定義した予約のオブジェクトを取得
        context['booking'] = Booking.objects.all()
        print('booking')
        # modelで定義したレビューのオブジェクトを取得
        context['review'] = Review.objects.all()
        print('review')
        # modelで定義したお気に入りのオブジェクトを取得
        context['favorite'] = Favorite.objects.all()
        print('favorite')

        return context