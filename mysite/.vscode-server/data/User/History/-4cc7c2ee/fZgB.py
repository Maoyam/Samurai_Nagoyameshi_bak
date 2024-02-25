from django.views.generic.edit import CreateView
from commondb.models.booking import Booking

class BookingCreateView(CreateView):
    model = Booking
    template_name = 'general/shop_detail.html'
    fields = ['booking_date', 'booking_time', 'numbers_of_ppl']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()  # フォームをコンテキストに追加
        return context