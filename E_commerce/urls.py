"""
URL configuration for E_commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from App import views
from django.conf import settings  
from django.conf.urls.static import static  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('blog/',views.blog,name='blog'),
    path('blog_details/',views.blog_details,name='blog_details'),
    path('shop/',views.shop,name='shop'),
    path('shop_details/',views.shop_details,name='shop_details'),
    path('shop_cart/',views.shop_cart,name='shop_cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),

]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
