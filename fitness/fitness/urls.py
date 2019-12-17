"""fitness URL Configuration

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
from gym.views import index,home,about,pricing,service,trainer,contact,blog,blog_sidebar,blog_single,course,course_single,sendmail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('home',home),
    path('about',about),
    path('pricing',pricing),
    path('service',service),
    path('trainer',trainer),
    path('contact',contact),
    path('blog',blog),
    path('blog_sidebar',blog_sidebar),
    path('blog_single',blog_single),
    path('course',course),
    path('course_single',course_single),
    path('sendmail',sendmail),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
