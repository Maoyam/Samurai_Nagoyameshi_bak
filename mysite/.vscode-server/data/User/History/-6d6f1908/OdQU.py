from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from commondb.models.booking import Booking

class BookingCreateView(CreateView):
    model = Booking
    template_name = 'shop_detail.html'
    fields = ['booking_date', 'booking_time', 'numbers_of_ppl']
    
    form = context['form']