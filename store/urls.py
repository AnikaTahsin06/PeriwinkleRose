from django.urls import path 
from .views.home import Index
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.khaltirequest import KhaltiRequest
from .views.orders import OrderView
from .views.about import About
from .views.ourstore import OurStore
from .views.search import Search
from .views.customerprofile import CustomerProfile
 


 

urlpatterns = [
    path('',  Index.as_view(), name='homepage'),
    path('signup',  Signup.as_view(), name='signup'),
    path('login',  Login.as_view(), name='login'),
    path('logout',  logout, name='logout'),
    path('cart',  Cart.as_view(), name='cart'),
    path('cheak-out',  CheckOut.as_view(), name='checkout'),
    path('khalti-request',  KhaltiRequest.as_view(), name='khaltirequest'),
    path('orders',  OrderView.as_view(), name='orders'),
    path('about',About.as_view(),name='about'),
    path('ourstore',OurStore.as_view(),name='ourstore'),
    path('search',Search.as_view(), name='search'),
    path('customerprofile',CustomerProfile.as_view(), name='customerprofile')
     
]