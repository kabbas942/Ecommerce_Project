from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
# Create your views here.
# view funtion for Login
def signin(request):
    if request.method=="POST":
        userName = request.POST.get('userEmail')
        userPassword = request.POST.get('userPassword')
        authenticateUser = authenticate(username=userName, password=userPassword)
        if authenticateUser is not None:
            login(request,authenticateUser)
            return redirect('/ecommerce')
        else:
            return render(request,'ecommerce/signIn.html')    
    return render(request,'ecommerce/signIn.html')
# View function for Creating New user
def signup(request):
    if request.method=="POST":
        userName= request.POST.get("userName")
        userEmail= request.POST.get("userEmail")
        userPassword= request.POST.get("userPassword")
        getUserModel=get_user_model()
        createUser = getUserModel.objects.create_user(username=userName, password=userPassword, email=userEmail)
        createUser.save()
        return render(request,"ecommerce/signIn.html")
    else:
        return render(request,"ecommerce/signUp.html")
#view function of logout
def logOutProfile(request):
    logout(request)
    return redirect('/ecommerce/signIn')
