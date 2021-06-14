from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('Pages.urls')),
    path('',include('Stores.urls')),
    path('',include('Account.urls')),
    path('',include('FAQ.urls')),
    path('',include('Contact.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
