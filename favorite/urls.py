from django.contrib import admin
from django.urls import path, include
from. import views
urlpatterns = [
    path('basket_adding', views.basket_adding, name='basket_adding'),
    path('checkout', views.checkout, name='checkout'),
    #path('basket_add',views.basket_add, name = 'basket_add'),
]