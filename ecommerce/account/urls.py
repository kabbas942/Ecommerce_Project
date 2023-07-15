from django.urls import path
from account import views

urlpatterns = [
    path('',views.signin,name="signin"),
    path('signup',views.signup,name="signup"),
    path('signout',views.signout,name="signout"),
]