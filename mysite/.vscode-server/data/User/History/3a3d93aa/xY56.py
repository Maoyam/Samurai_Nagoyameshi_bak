from django.shortcuts import render
from django.views.generic import CreateView
from commondb.models.company import Company

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Company
    fields = '__all__'
        
