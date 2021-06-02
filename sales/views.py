from django.shortcuts import render

# Create your views here.

# M - models
# V - views
# T - templates


def home_view(request):
    hello = "hello world from the view"
    return render(request, 'sales/home.html', {'hello': hello})
