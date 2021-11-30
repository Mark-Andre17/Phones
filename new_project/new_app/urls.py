from django.contrib import admin
from django.urls import path, include
from .views import show_product, show_catalog, index

urlpatterns = [
    path('', index),
    path('catalog/', show_catalog, name='catalog'),
    path('catalog/<slug:slug>/', show_product, name='phone')
]
