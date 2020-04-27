from django.contrib import admin
from .models import *


class ProductInFavoriteInline(admin.TabularInline):
    model = ProductInFavorite
    extra = 0



class StatusAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)


class FavoriteAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Favorite._meta.fields]
    inlines = [ProductInFavoriteInline]

    class Meta:
        model = Favorite

admin.site.register(Favorite, FavoriteAdmin)


class ProductInFavoriteAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInFavorite._meta.fields]

    class Meta:
        model = ProductInFavorite

admin.site.register(ProductInFavorite, ProductInFavoriteAdmin)

class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]

    class Meta:
        model = ProductInBasket

admin.site.register(ProductInBasket, ProductInBasketAdmin)