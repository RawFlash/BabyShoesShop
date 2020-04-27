from django.contrib import admin
from django.urls import path, include
from beautysaves import views

urlpatterns = [
    path('', views.home,name='home'),
    path('buy',views.buy,name = "buy"),
    path('end_buy', views.end_buy, name = 'end_buy')
    #path('beautysaves', views.beautysaves,name='beautysaves')
]