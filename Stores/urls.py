from django.urls import path
from .import views

urlpatterns = [
    path('jeans',views.jeans,name='jeans'),
    path('polo',views.polo,name='polo'),
    path('shirts',views.shirts,name='shirts'),
    path('suites',views.suites,name='suites'),
    path('t_shirts',views.t_shirts,name='t_shirts')
]
