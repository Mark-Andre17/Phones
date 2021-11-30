from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'id')
    sort_sources = {
        'name': 'name',
        'lowprice': 'price',
        'maxprice': '-price',
        'id': 'id',
    }
    if sort not in sort_sources.keys():
        sort = 'id'
    phones = Phone.objects.order_by(sort_sources[sort]).all()
    context = {'phones': phones,
               'sort': sort,
               }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).get()
    context = {
        'phone': phone,
    }
    return render(request, template, context)
