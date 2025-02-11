
from django.urls import path, include
from Authication import views
urlpatterns = [

    path('',views.Login, name="Login"),
    path('OTP/', views.OTP, name="OTP"),
    path('Signup/', views.SignUp, name="SignUp")


]