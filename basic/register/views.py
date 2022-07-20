from django.shortcuts import render, redirect
from register.forms import RegisterForm
# from django.contrib.auth import login,authenticate

# Create your views here.
def register(request):
    
    if request.method == "POST":
        form = RegisterForm()
        if form.is_valid():
            form.save()
            return redirect("/home")
    
        else:
            form = RegisterForm()
    return render(request, "register.html",{"form":form})   


def index(request):
    return render (request, 'index.html')
	