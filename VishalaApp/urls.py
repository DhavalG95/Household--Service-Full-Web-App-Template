from django.urls import path 
from .views import *

urlpatterns = [
   
    path('',home,name="home"),
    path('login',login,name="login"),
    path('logout',logout,name="logout"),
    path('service',service,name="service"),
    path('contact',contact,name="contact"),
    path('payment/<int:pk>',payment,name="payment"),
    path('success',success,name="success"),

]
