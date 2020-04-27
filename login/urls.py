from django.urls import path, include
from django.contrib import admin
from products import views
from . import views

urlpatterns = [
    #Добавление продукта в заказ
    path('login/add',views.add, name = 'add'),

    #Добавление продукта в каталог
    path('login/add_product',views.add_product, name = 'add_product'),
    path('login/', views.login, name='login'),
    path('login/out/', views.out, name= 'out'),

]