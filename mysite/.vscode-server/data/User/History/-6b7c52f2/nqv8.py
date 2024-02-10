from django.views.generic import TemplateView

class TopView(TemplateView):
    template_name = "general/index.html"
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
            
        areas = Areas.object.all()

        context['areas'] = areas

        return contex