from django import forms
from products.models import ProductImage, Product


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price')

class NewProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ('product', 'image')