from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','email')
    list_display_links = ('name',)
admin.site.register(Contact, ContactAdmin)
