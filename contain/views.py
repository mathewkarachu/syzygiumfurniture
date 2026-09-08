from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout,authenticate,decorators


import re

@decorators.login_required
def Home(request):
    return render(request,"index.html")

def Login(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            
            if user.is_superuser:
                return redirect("admin:index")
            
            
            
            return redirect('home')
        
        
        
        else:
            messages.error(request, "Invalid username or password")
        
    
    
    
    return render(request,"login.html")

def Signup(request):
    if request.method =="POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        user_data_has_error = False
        
        
        if User.objects.filter(username = username).exists():
            
            user_data_has_error =   True
            
            messages.error(request,"User already exists!")
        elif User.objects.filter(email=email).exists():
            
            user_data_has_error = True;
            
            messages.error(request, "Email already exists!!")
        elif password != password2:
            user_data_has_error = True
            messages.error(request, "Passwords do not match!")
        elif len(password) < 5:
            user_data_has_error = True;
            messages.error(request, "Password must be at least 5 characters.")

        elif not re.search(r"[A-Z]", password):
            user_data_has_error = True;
            messages.error(request, "Password must contain at least one uppercase letter.")

        elif not re.search(r"[a-z]", password):
            messages.error(request, "Password must contain at least one lowercase letter.")
            user_data_has_error = True;

        elif not re.search(r"\d", password):
            messages.error(request, "Password must contain at least one number.")
            user_data_has_error = True;

        elif not re.search(r"[^A-Za-z0-9]", password):
            messages.error(request, "Password must contain at least one special character.")
            user_data_has_error = True;
            
            
        elif user_data_has_error:
            return redirect('register')
            
        
        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
                
            )
            
            return redirect('login')
        
        
        
    
    
    return render(request, "signup.html")
# Create your views here.


def Logout(request):
    logout(request)
    return redirect("home")

