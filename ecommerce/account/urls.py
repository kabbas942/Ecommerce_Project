from django.urls import path
from account import views

urlpatterns = [
    path('',views.signin,name="signIn"),
    path('signup',views.signup,name="signUp"),
    path('signout',views.signout,name="signout"),
    path('profile',views.profile,name="profile"),
    path('settings',views.settings,name="settings"),
]