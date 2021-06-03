from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Sale

from .forms import SalesSearchForm

import pandas as pd

# Create your views here.

# M - models
# V - views
# T - templates


def home_view(request):
    form = SalesSearchForm(request.POST or None)

    date_from= None
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')

        print(date_from, date_to, chart_type)

        qs = Sale.objects.all()
        qs = Sale.objects.filter(created__date=date_from)
        obj = Sale.objects.get(id=1)
        print(obj)
        print(qs)
        print(qs.values())
        print(qs.values_list())
        print("==================================")
        print("==================================")
        df1 = pd.DataFrame(qs.values())
        print(df1)
        print("==================================")
        print("==================================")
        df2 = pd.DataFrame(qs.values_list())
        print(df2)

    context = {
        'form': form
    }
    return render(request, 'sales/home.html', context)


class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
    #context_object_name = 'qs'


class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'


def sale_list_view(request):
    qs = Sale.objects.all()
    return render(request, 'sales/main.html', {'object_list': qs})


#def sale_detail_view(request, pk):
def sale_detail_view(request, **kwargs):
    pk = kwargs.get('pk')
    obj = Sale.objects.get(pk=pk)
    #obj = get_object_or_404(Sale, pk=pk)
    return render(request, 'sales/detail.html', {'object': obj})
