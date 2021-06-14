from django.shortcuts import render
from .models import Jean, Polo, Shirts, Suites, T_shirts
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def jeans(request):
    jeans = Jean.objects.order_by('-list_date')
    paginator = Paginator(jeans,4)
    page = request.GET.get('page')
    paged_jeans = paginator.get_page(page)

    context = {
        'jeans':paged_jeans
    }
    return render(request, 'stores/jeans.html', context)

def polo(request):
    polos = Polo.objects.order_by('-list_date')
    paginator = Paginator(polos,4)
    page = request.GET.get('page')
    paged_polos = paginator.get_page(page)

    context = {
        'polos':paged_polos
    }
    return render(request, 'stores/polo.html', context)

def shirts(request):
    shirts = Shirts.objects.order_by('-list_date')
    paginator = Paginator(shirts,4)
    page = request.GET.get('page')
    paged_shirts = paginator.get_page(page)

    context = {
        'shirts':paged_shirts
    }
    return render(request, 'stores/shirts.html', context)

def suites(request):
    suites = Suites.objects.order_by('-list_date')
    paginator = Paginator(suites,4)
    page = request.GET.get('page')
    paged_suites = paginator.get_page(page)

    context = {
        'suites':paged_suites
    }
    return render(request, 'stores/suites.html', context)

def t_shirts(request):
    t_shirts = T_shirts.objects.order_by('-list_date')
    paginator = Paginator(t_shirts,8)
    page = request.GET.get('page')
    paged_t_shirts = paginator.get_page(page)

    context = {
        't_shirts':paged_t_shirts
    }
    return render(request, 'stores/t-shirts.html', context)
