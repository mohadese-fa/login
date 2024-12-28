"""
URL configuration for pamir_trade project.

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
from main_app.views import index,product_category,products,shop,agency,about,contact_us,question,agencyCity,account,login
from django.conf import settings
from django.conf.urls.static import static
from main_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('login/', login, name='login'),
    path('account/', account),
    path('product_category/', product_category),
    path('products/<num>', products),
    path('shop/<num>', shop),
    path('agency/', agency),
    path('agencyCity/<num>', agencyCity),
    path('about/', about),
    path('contact_us/', contact_us),
    path('question/', question),    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
