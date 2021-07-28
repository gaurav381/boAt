from django import views
from django.contrib import admin
from django.urls import path
from .views.home import pro , store ,home ,plu
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut,handlerequest
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', pro.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('home', home, name='home'),
    path('plu-in-sale', plu, name='plu'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('handlerequest',handlerequest, name='handlerequest'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),

]
