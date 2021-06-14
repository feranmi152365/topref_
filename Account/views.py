from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User

def account(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Email = request.POST['Email']
        Password = request.POST['Password']
        Password2 = request.POST['Password2']

        # Password Validation
        if Password == Password2:
            # Check Username
            if User.objects.filter(Username=Username).exists():
                messages.error(request,'Username already exist')
                return redirect('signin')
            else:
                if User.objects.filter(Email=Email).exists():
                    messages.error(request,'Email already exist')
                    return redirect('signin')
                else:
                    return
            
        else:
            messages.error(request, 'Password do not match')
            return redirect('Polo')
    else:


        return render(request, 'account/signin.html')
