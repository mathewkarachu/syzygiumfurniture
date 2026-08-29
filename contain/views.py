from django.shortcuts import render


def Home(request):
    return render(request,"index.html")

def Login(request):
    return render(request,"login.html")

def Signup(request):
    return render(request, "signup.html")
# Create your views here.
