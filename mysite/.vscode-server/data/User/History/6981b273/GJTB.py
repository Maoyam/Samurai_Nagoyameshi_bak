from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

class LogoutView(LogoutView):
    template_name = 'general/top.html'