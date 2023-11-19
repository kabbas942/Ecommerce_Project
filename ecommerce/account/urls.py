from django.urls import path
from account import views

urlpatterns = [
    path('',views.signin,name="signin"),
    path('signup',views.signup,name="signup"),
    path('logout',views.logOutProfile,name="logout"),
]