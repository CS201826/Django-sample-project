"""sampleproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from products.views import *

urlpatterns = [
    url(r'^categories$', CategoryList.as_view(), name='category-list'),
    url(r'^category/create$', CategoryCreate.as_view(), name='category-create'),
    url(r'^category/edit/(?P<pk>\d+)$', CategoryUpdate.as_view(), name='category-update'),
    url(r'^category/delete/(?P<pk>\d+)$', CategoryDelete.as_view(), name='category-delete'),
    url(r'^products$', ProductList.as_view(), name='product-list'),
    url(r'^product/create$', ProductCreate.as_view(), name='product-create'),
    url(r'^product/edit/(?P<pk>\d+)$', ProductUpdate.as_view(), name='product-update'),
    url(r'^product/delete/(?P<pk>\d+)$', ProductDelete.as_view(), name='product-delete')
]
