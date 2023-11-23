from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib import messages
# Create your views here.
# view funtion for Login
def signin(request):
    if request.method=="POST":
        userName = request.POST.get('userEmail')
        userPassword = request.POST.get('userPassword')
        authenticateUser = authenticate(username=userName, password=userPassword)
        if authenticateUser is not None:
            login(request,authenticateUser)
            return redirect('/')
        else:
            messages.warning(request,"Your email or password is incorrect")
            return render(request,'ecommerce/signIn.html')    
    return render(request,'ecommerce/signIn.html')
# View function for Creating New user
def signup(request):
    if request.method=="POST":
        name= request.POST.get("name")
        userEmail= request.POST.get("userEmail")
        userPassword= request.POST.get("userPassword")
        print(request.POST)
        getUserModel=get_user_model()
        createUser = getUserModel.objects.create_user(username=userEmail, password=userPassword, first_name=name)
        
        if createUser:
            messages.success(request,"Your Account Created Successfully")
            return redirect("/account/complete")
        else:
            messages.warning(request,"Failed to Create")
            return render(request,"ecommerce/signUp.html")
    else:
        return render(request,"ecommerce/signUp.html")
#view function of logout
def logOutProfile(request):
    logout(request)
    return redirect('/')

def complete(request):
    return render(request,'ecommerce/Comp_Otp.html')
