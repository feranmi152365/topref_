from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method=='POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.save()
        messages.success(request, 'Your request has been submitted')
        return redirect('index')
    return render(request, 'Pages/index.html')
