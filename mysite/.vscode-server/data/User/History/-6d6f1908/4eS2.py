from django.views.generic.edit import CreateView
from commondb.models.booking import Booking

class BookingCreateView(CreateView):
    model = Booking
    template_name = 'general/shop_detail.html'
    fields = ['booking_date', 'booking_time', 'numbers_of_ppl']