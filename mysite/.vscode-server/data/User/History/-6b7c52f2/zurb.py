from typing import Any
from django.views.generic import TemplateView
from ..models.area import Area
from ..models.genre import Genre

class TopView(TemplateView):
    template_name = "general/index.html"
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
            
        areas = Area.objects.all()

        context['areas'] = areas

        return context
    
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        
        genres = Genre.objects.all()
        
        context['genres'] = genres
        return context
    