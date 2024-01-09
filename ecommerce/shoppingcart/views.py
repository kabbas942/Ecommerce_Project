from django.shortcuts import render,HttpResponse,redirect
from shoppingcart.models import Product,Category,Order,OrderDetail
from django.contrib import sessions
from django.db.models import Count


#main page
def index(request):
    allProductList= Product.objects.all()
    categoryList= Category.objects.all()
    productPara={}
    for category in categoryList:
        productListByCategories = Product.objects.filter(productCategory= category.categoryId)[:10]
        if productListByCategories:
            productParameter=productPara.update({category.categoryName: productListByCategories})     
    productParameter={'products':productPara}
    return render(request,"ecommerce/index.html",productParameter)


def productDescription(request,productDescriptionId):
    productInfo = Product.objects.get(productId = productDescriptionId)
    productInfo = {'productInformation':productInfo}
    return render(request,"ecommerce/productDescription.html",productInfo)


def contact(request):
    return render(request,"ecommerce/contact.html")


#Categories the  Product
def productCategories(request,categoryId):
    productInfo = Category.objects.get(categoryName = categoryId)
    productCategoryInfo = Product.objects.filter(productCategory= productInfo.categoryId)
    productInformations = {'productInformations':productCategoryInfo,'category':categoryId}
    return render(request,"ecommerce/productCategories.html",productInformations)


#Searching Product
def search(request):
    if request.method == 'GET':
        query = request.GET.get('productSearch')  # Get the search query from the request's GET parameters
        productList = Product.objects.filter(productName__icontains=query)  # Perform case-insensitive search on the 'name' field
        if productList:
            productList = productList | Product.objects.filter(productDescription__icontains=query)
            productList = productList | Product.objects.filter(productCategory__categoryName__icontains=query)
            productParameter={'products':productList,'search': query}
        else:
            productList = Product.objects.filter(productCategory__categoryName__icontains=query)
            productParameter={'products':productList,'search': query}
        return render(request,"ecommerce/search.html",productParameter)
    return redirect("/ecommerce")


def shippingAddress(request):
        if request.method == 'POST':
            customerName = request.POST.get("shippingAddress")
            shippingAddress=request.POST.get("shippingAddress")
            mobileNumber=request.POST.get("mobileNumber")
            countryName=request.POST.get("countryName")
            stateName=request.POST.get("stateName")
            zipCode=request.POST.get("zipCode")
            OrderNow= Order(customerName=customerName,orderAddress=shippingAddress,orderCountry=countryName,orderState=stateName,orderZipCode=zipCode,orderMobileNumber=mobileNumber,orderPrice=33)
            OrderNow.save()
            for productDetailId,Qty in request.session['cart'].items(): 
                product= Product.objects.get(productId=productDetailId)          
                orderId = Order.objects.get(orderId = OrderNow.pk) 
                OrderDetailNow = OrderDetail(productId=product, orderId=orderId, orderProductQuantity=Qty,productPrice=product.productPrice)
                OrderDetailNow.save()                
            request.session.flush()            
        return render(request,"ecommerce/shippingAddress.html")


#Viewing Cart
def cartView(request):
    if request.session.get('cart'):        
        cartString = request.session['cart'].keys()
        cartDictionary = {int(key): value for key, value in request.session['cart'].items()}
        cartInt= [int(x) for x in cartString]
        cartProductsPrice = []
        cartPriceDictionary = {}
        for y in cartInt:
            productPrice = cartDictionary.get(y) * Product.objects.get(productId = y).productPrice
            cartPriceDictionary[y]=productPrice
            cartProductsPrice.append(productPrice)
        cartProducts = {'cartProducts':Product.objects.filter(productId__in = cartInt), 'cartDictionary':cartDictionary,'total':sum(cartProductsPrice),'productPriceList':cartPriceDictionary}
        return render(request,'ecommerce/cart.html',cartProducts)
    else:
        return render(request,'ecommerce/cart.html')


#Adding Product in Cart (Session) 
def cart(request):
    if request.method=="POST":
        cartId = int(request.POST.get("cartId"))        
        cartValue = request.session.get('cart')
        if cartValue:
            quantity = cartValue.get(cartId)
            if quantity:
                cartValue[cartId] = quantity + 1
            else:
                cartValue[cartId] = 1
        else:
            cartValue = {} 
            cartValue[cartId] = 1  
        request.session['cart']=cartValue
        totalCartQuantity = sum(request.session['cart'].values())    
        request.session['quantity']=totalCartQuantity
        print(totalCartQuantity)
        return redirect(request.META.get('HTTP_REFERER')) #redirect a user back to the page they came from


#Update Product Quantity in Cart (Session)    
def cartUpdateQty(request):
    if request.method=="POST":
        #get dictionary from cart quantity control
        for key, value in request.POST.items():
            if key.startswith('cartProductId_'):
                cartProductId=value   
               
            if key.startswith('cartUpdateQuantity_'):
               updateQuantity = value    
         #get session and store in cart                        
        cartValue = request.session.get('cart')
        if cartValue:
           cartValue[cartProductId] =int(updateQuantity)                      
        request.session['cart']=cartValue
        totalCartQuantity = sum(request.session['cart'].values())
        request.session['quantity']=totalCartQuantity      
    return redirect("/ecommerce/cartView")


#Delete Product from Cart (Session)
def deleteCartProduct(request):
    if request.method=="POST":
        #get dictionary from cart quantity control
        for key, value in request.POST.items():
            if key.startswith('deleteCartProductId_'):
                if request.session['quantity']!=0:
                    request.session['quantity']=request.session['quantity']-request.session['cart'][str(value)]
                del request.session['cart'][value]  
                request.session.modified = True  
    return redirect("/ecommerce/cartView")