from django.contrib import admin
from django.urls import path,include
from shoppingcart import views

urlpatterns = [
    path('',views.index,name="Home"),
    path('ecommerce/categories/<str:categoryId>',views.productCategories,name="productCategories"),
    path('ecommerce/contact/',views.contact,name="contact"),
    path('ecommerce/search/',views.search,name="Search"),    
    path('ecommerce/cart/',views.cart,name="Cart"),
    path('ecommerce/cartDelete/',views.deleteCartProduct,name="deleteCartProduct"),
    path('ecommerce/order/',views.order,name="order"),
    path('ecommerce/cartView/',views.cartView,name="cartView"),
    path('ecommerce/productDescription/<int:productDescriptionId>/',views.productDescription,name="productDescription"),
    path('ecommerce/cartUpdate/',views.cartUpdateQty,name="cartUpdateQty"),
]
