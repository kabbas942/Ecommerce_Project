from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.urls import reverse
from django.contrib.auth.models import User
from shoppingcart.models import Order,OrderDetail,Product
# Create your views here.

def signin(request):
    if request.method=="POST":
        userName = request.POST.get('userEmail')
        userPassword = request.POST.get('userPassword')
        authenticateUser = authenticate(username=userName, password=userPassword)
        if authenticateUser is not None:
            login(request,authenticateUser)
            return redirect('/')
        else:
            return render(request,'account/signIn.html')
    return render(request,"account/signIn.html")

def signup(request):
    if request.method=="POST":
        Name= request.POST.get("userName")
        username= request.POST.get("userEmail")
        userPassword= request.POST.get("userPassword")
        getUserModel=get_user_model()
        createUser = getUserModel.objects.create_user(username=username, password=userPassword, first_name=Name)
        createUser.save()
        return redirect(reverse('signIn'))
    return render(request,"account/signUp.html")

def profile(request):
    return render(request,"account/profile.html")

def settings(request):
    return render(request,"account/setting.html")

def signout(request):
    logout(request)
    return redirect('/')

def shippingAddress(request):
        if request.method == 'POST':
            userId = User.objects.get(id=request.user.id)
            shippingAddress=request.POST.get("shippingAddress")
            mobileNumber=request.POST.get("mobileNumber")
            OrderNow= Order(customerId=userId,orderAddress=shippingAddress,orderMobileNumber=mobileNumber,orderPrice=33)
            OrderNow.save()
            for productDetailId,Qty in request.session['cart'].items(): 
                product= Product.objects.get(productId=productDetailId)          
                orderId = Order.objects.get(orderId = OrderNow.pk) 
                OrderDetailNow = OrderDetail(productId=product, orderId=orderId, orderProductQuantity=Qty,productPrice=product.productPrice)
                OrderDetailNow.save()                
            request.session.flush()            
            return render(request,"ecommerce/shippingAddress.html")







'''
def shippingAddress(request):
    if request.user.is_anonymous:
        return redirect('/account/')   
    else:
        if request.method == 'POST':
            userId = User.objects.get(id=request.user.id)
            shippingAddress=request.POST.get("shippingAddress")
            mobileNumber=request.POST.get("mobileNumber")
            OrderNow= Order(customerId=userId,orderAddress=shippingAddress,orderCountry=countryName,orderState=stateName,orderZipCode=zipCode,orderMobileNumber=mobileNumber,orderPrice=33)
            OrderNow.save()
            for productDetailId,Qty in request.session['cart'].items(): 
                product= Product.objects.get(productId=productDetailId)          
                orderId = Order.objects.get(orderId = OrderNow.pk) 
                OrderDetailNow = OrderDetail(productId=product, orderId=orderId, orderProductQuantity=Qty,productPrice=product.productPrice)
                OrderDetailNow.save()                
            request.session.flush()            
            return render(request,"ecommerce/shippingAddress.html")





'''