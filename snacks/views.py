from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Snack

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SnackListView(ListView):
    model = Snack
    template_name = 'snack_list.html'

class SnackDetailView(DetailView):
    model = Snack
    template_name = 'snack_detail.html'

class SnackListView(ListView):
    model = Snack
    template_name = 'snack_list.html'

class SnackDetailView(DetailView):
    model = Snack
    template_name = 'snack_detail.html'