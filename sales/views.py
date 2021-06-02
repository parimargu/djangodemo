from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Sale

# Create your views here.

# M - models
# V - views
# T - templates


def home_view(request):
    hello = "hello world from the view"
    return render(request, 'sales/home.html', {'hello': hello})


class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
    #context_object_name = 'qs'

class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'