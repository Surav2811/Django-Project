from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from .forms import CustomUserCreationForm  
# Create your views here.  
  
def register(request):  
    if request.POST == 'POST':  
        form = CustomUserCreationForm()  
        if form.is_valid():  
            form.save()  
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'register.html')  