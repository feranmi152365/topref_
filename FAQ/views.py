from django.shortcuts import render
from .models import Faqs

def faq(request):
#     faqs = Faqs.objects.all()
# 
#     context = {
#         'faqs':faqs
#     }
    return render(request, 'Pages/index.html')