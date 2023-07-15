from django.shortcuts import render,HttpResponse

# Create your views here.

def signin(request):
    return render(request,"ecommerce/signin.html")

def signup(request):
    return render(request,"ecommerce/signup.html")

def signout(request):
    return HttpResponse("Signout")
