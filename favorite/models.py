from django.db import models
from django.db.models.signals import post_save
from products.models import Product
import django.db.models.options as options
from django.contrib.auth.models import User

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('save',)


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус фаворита'
        verbose_name_plural = 'Статусы фаворита'


class Favorite(models.Model):
   # user = models.ForeignKey(m.LoginUser,on_delete=models.PROTECT, blank=True, null=True, default=None)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,
                                      default=0)  # total price for all products in order
    girl_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    girl_email = models.EmailField(blank=True, null=True, default=None)
    girl_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    store_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status,on_delete=models.PROTECT,  default=1)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Фаворит %s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Фаворит'
        verbose_name_plural = 'Фавориты'

        def save(self, *args, **kwargs):
            super(Favorite, self).save(*args, **kwargs)





class ProductInFavorite(models.Model):
    favorites = models.ForeignKey(Favorite
                                  ,on_delete=models.CASCADE
                                  , blank=True, null=True,  default=1)
    product = models.ForeignKey(Product,on_delete=models.PROTECT, blank=True, null=True,  default=1)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Товар в фаворитах'
        verbose_name_plural = 'Товары в фаворитах'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price =int (self.nmb) * price_per_item

        super(ProductInFavorite, self).save(*args, **kwargs)

def product_in_favorites_post_save(sender, instance, created, **kwargs):
    favorites = instance.favorites
    all_products_in_favorites = ProductInFavorite.objects.filter(favorites=favorites, is_active=True)

    favorites_total_price = 0
    for item in all_products_in_favorites:
        favorites_total_price += item.total_price

    instance.favorites.total_price = favorites_total_price
    instance.favorites.save(force_update=True)

post_save.connect(product_in_favorites_post_save, sender=ProductInFavorite)




class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    favorites = models.ForeignKey(Favorite,on_delete=models.CASCADE, blank=True, null=True,  default=1)
    product = models.ForeignKey(Product,on_delete=models.PROTECT, blank=True, null=True,  default=1)
    nmb = models.IntegerField(default=1 ,null=True)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Фавориты в списке'
        verbose_name_plural = 'Фавориты в списке'

   # def save(self, *args, **kwargs):
       # price_per_item = self.product.price
       # self.price_per_item = price_per_item
       # self.total_price = int(self.nmb) * price_per_item

        #super(ProductInBasket, self).save(*args, **kwargs)

