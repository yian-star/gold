"""
URL configuration for gold project.

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
from customer import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('customer/add', views.add_customer, name='add_customer'),
    path('customer/query', views.query_customer, name='query_customer'),
    path('customer/update', views.update_view, name='update_view'),
    path('customer/delete', views.delete_view, name='delete_view')
]
