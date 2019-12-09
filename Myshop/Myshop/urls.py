"""Myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Garments.views import index,aboutus,contactus,formalshirts,casualshirts,shorts,jeans,casualshirts_w,formalshirts_w,jeans_w,shorts_w,search_list,wishlist,registration,thankyou
from Garments.views import setsession,getsession,login
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('',index),
    path('aboutus',aboutus),
    path('contactus',contactus),
    path('formalshirts',formalshirts),
    path('casualshirts',casualshirts),
    path('shorts',shorts),
    path('jeans',jeans),
    path('formalshirts_w',formalshirts_w),
    path('casualshirts_w',casualshirts_w),
    path('jeans_w',jeans_w),
    path('shorts_w',shorts_w),
    path('search_list',search_list),
    path('wishlist',wishlist),
    path('registration',registration),
    path('login',login),
    path('thankyou',thankyou),
   # path('cart<int:x>',cart),
    path('setsession',setsession),
    path('getsession',getsession),
   # path('setcookie',setcookie),
    #path('getcookie',getcookie),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
