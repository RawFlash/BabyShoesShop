from django.urls import path, include
from django.contrib import admin
from products import views

urlpatterns = [
    # url(r'^landing123/', views.landing, name='landing'),
    path('product/<product_id>/', views.product, name='product'),
]