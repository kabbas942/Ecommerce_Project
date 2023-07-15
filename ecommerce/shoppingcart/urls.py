from django.contrib import admin
from django.urls import path,include
from shoppingcart import views

urlpatterns = [
    path('',views.index,name="Home"),
    path('ecommerce/categories/<str:categoryId>',views.productCategories,name="productCategories"),
    path('ecommerce/contact/',views.contact,name="Contact"),
    path('ecommerce/search/',views.search,name="Search"),    
    path('ecommerce/cart/',views.cart,name="Cart"),
    path('ecommerce/cartDelete/',views.deleteCartProduct,name="deleteCartProduct"),
    path('ecommerce/shippingAddress/',views.shippingAddress,name="shippingAddress"),
    path('ecommerce/cartView/',views.cartView,name="cartView"),
    path('ecommerce/productDescription/<int:productDescriptionId>/',views.productDescription,name="productDescription"),
    path('ecommerce/cartUpdate/',views.cartUpdateQty,name="cartUpdateQty"),
    path('ecommerce/signUp/',views.signUp,name="signUp"),
    path('ecommerce/signIn/',views.signIn,name="signIn"),
    path('ecommerce/logOut/',views.logOutProfile,name="signOut"),
]
