from django.shortcuts import render
from .models import Faqs
from Stores.models import Jean,Polo,Suites,T_shirts,Shirts

def index(request):
    jeans = Jean.objects.order_by('list_date')[:4]
    polos = Polo.objects.order_by('list_date')[:4]
    suites = Suites.objects.order_by('list_date')[:4]
    t_shirts = T_shirts.objects.order_by('list_date')[:4]
    shirts = Shirts.objects.order_by('list_date')[:4]
    faqs = Faqs.objects.all()

    context = {
        'faqs':faqs,
        'jeans':jeans,
        'polos':polos,
        't_shirts':t_shirts,
        'suites':suites,
        'shirts':shirts
    }
    return render(request, 'Pages/index.html' ,context)
