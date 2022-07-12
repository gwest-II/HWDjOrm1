from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from phones.models import Phone
from django.http import HttpResponseNotFound, HttpResponse
from django.urls import reverse


def index(request):
    template = 'index.html'

    pages = {
        'Домашняя страница': reverse('index'),
        'Каталог телефонов': reverse('catalog')
    }
    context = {
        'pages': pages
    }

    return render(request, template, context)


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', '')
    if sort == 'name':
        phones = Phone.objects.order_by('name')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')
    else:
        phones = Phone.objects.all()

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    try:
        phone = Phone.objects.get(slug=slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('Phone does not exist')
    context = {
        'phone': phone
    }
    return render(request, template, context)
