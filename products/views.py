from django.shortcuts import render
from products.models import *
from favorite import models as FavModels


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        print(request.session.session_key)

    try:
        if request.COOKIES.get("id_user") != 'None':
            print("cookie work")
            is_login = True
        else:
            is_login = False
    except:
        is_login = False

    id_user = request.COOKIES.get('id_user')
    products = FavModels.ProductInBasket.objects.filter(session_key=id_user)
    products_total_nmb = products.count()

    product.id = product.id
    product.name = product.name
    product.price = product.price
    is_login = True
    is_admin=False

    return render(request, 'products/products.html', locals())
