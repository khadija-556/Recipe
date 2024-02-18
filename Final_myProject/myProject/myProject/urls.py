"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', singupPage,name="singupPage"),
    path('singinPage/', singinPage,name="singinPage"),
    path('logoutPage/', logoutPage,name="logoutPage"),
    path('homePage/', homePage,name="homePage"),
    path('forget_pass/', forget_pass,name="forget_pass"),
    path('update_pass/', update_pass,name="update_pass"),
    path('Recipi_catagories/', Recipi_catagories,name="Recipi_catagories"),
    path('Recipi/', Recipi,name="Recipi"),
    path('viewRecipi/', viewRecipi,name="viewRecipi"),
    path('editRecipi/<str:id>', editRecipi,name="editRecipi"),
    path('RecipiDeletePage/<str:id>', RecipiDeletePage,name="RecipiDeletePage"),
    path('search_results/', search_results, name='search_results'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
