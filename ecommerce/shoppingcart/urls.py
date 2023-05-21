from django.contrib import admin
from django.urls import path,include
from shoppingcart import views

urlpatterns = [
    path('',views.index,name="Home"),
    path('categories/<str:categoryId>',views.productCategories,name="productCategories"),
    path('contact/',views.contact,name="Contact"),
    path('search/',views.search,name="Search"),    
    path('cart/',views.cart,name="Cart"),
    path('cartDelete/',views.deleteCartProduct,name="deleteCartProduct"),
    path('shippingAddress/',views.shippingAddress,name="shippingAddress"),
    path('cartView/',views.cartView,name="cartView"),
    path('productDescription/<int:productDescriptionId>/',views.productDescription,name="productDescription"),
    path('cartUpdate/',views.cartUpdateQty,name="cartUpdateQty"),
    path('signUp/',views.signUp,name="signUp"),
    path('signIn/',views.signIn,name="signIn"),
    path('logOut/',views.logOutProfile,name="signOut"),
]
