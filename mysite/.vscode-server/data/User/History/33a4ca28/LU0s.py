from typing import Any
from django.views.generic import TemplateView

class MypageView(TemplateView):
    template_name = "general/mypage.html"
    
    # def get_context_data(self, **kwargs: Any):
    #     context = super().get_context_data(**kwargs)
    #     # modelで定義したエリアのオブジェクトを取得
    #     context['areas'] = Area.objects.all()
    #     # modelで定義したジャンルのオブジェクトを取得
    #     context['genres'] = Genre.objects.all()

    #     return context