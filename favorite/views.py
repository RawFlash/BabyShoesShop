from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import *
from django.shortcuts import render
from .forms import CheckoutContactForm
from django.contrib.auth.models import User
from  login import models as LoginModels
from django.shortcuts import redirect

class ConvertProduct():
    name =str
    price = int
    number = int
    id = int
    def __init__(self,name,price,nmb,id):
        self.name=name
        self.price=price
        self.number=nmb
        self.id = id


def basket_adding(request):

    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("number")


    is_delete = data.get("is_delete")
    delete_id = data.get('delete_product_id')


    id_user = request.COOKIES.get('id_user')
    if id_user == "None":
        return redirect('http://127.0.0.1:8000')

    User = LoginModels.LoginUser.objects.get(id=id_user)

    id_fav=User.favorite.id

    if is_delete == 'true':
        ProductInBasket.objects.get(id=delete_id).delete()
        print("Удалил продукт")
    else:
        #price = Product.objects.get(id=product_id).price
        ProductInBasket.objects.create(session_key=id_user,product_id=product_id, nmb=nmb,favorites_id=id_fav)
        print("Добавил продукт")


    #products_in_basket = ProductInBasket.objects.filter(session_key=id_user)

    #products={}
   # print(str(products_in_basket.count()))
    #products['products_total_nmb'] = products_in_basket.count()
    #products['products']=[]

    #for i in  range(len(products_in_basket)):
        #products['products'].append()
        #products['products'][i]={"name"}
        #name = products_in_basket[i].product.name
        #price  =products_in_basket[i].price_per_item
        #number = products_in_basket[i].nmb
        #id=products_in_basket[i].id
        #list.append(ConvertProduct(name,price,number,id))

    id_user = request.COOKIES.get('id_user')
    products = ProductInBasket.objects.filter(session_key=id_user)
    products_total_nmb=products.count()



    try:
            if request.COOKIES.get("id_user")!='None':
                print("cookie work")
                is_login=True
            else:
                is_login=False
    except:
        is_login=False

    response = redirect('http://127.0.0.1:8000')
    #response = render(request,'beautysaves/home.html')
    return response



def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, favorites__isnull=True)
    print (products_in_basket)
    for item in products_in_basket:
        print(item.favorites)


    form = CheckoutContactForm(request.POST or None)
    if request.POST:

        id_user = request.COOKIES.get('id_user')

        id_fav = LoginModels.LoginUser.objects.get(id=id_user).favorite.id
        ProductInBasket.objects.filter(favorites_id=id_fav).delete()
        print("Удалил продукт")

        return redirect('http://127.0.0.1:8000')
        print(request.POST)
        if form.is_valid():
            print("yes")
            data = request.POST
            name = data.get("name", "3423453")
            phone = data["phone"]
            user, created = User.objects.get_or_create(username=phone, defaults={"first_name": name})

            favorites = Favorite.objects.create(user= user,girl_name=name,girl_phone=phone,status_id=1)

            for name, value in data.items():
                if name.startswith("product_in_basket_"):
                    product_in_basket_id = name.split("product_in_basket_")[1]
                    product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
                    print(type(value))

                    product_in_basket.nmb = value
                    product_in_basket.favorites = favorites
                    product_in_basket.save(force_update=True)

                    ProductInFavorite.objects.create(product=product_in_basket.product, nmb = product_in_basket.nmb,
                                                  price_per_item=product_in_basket.price_per_item,
                                                   total_price = product_in_basket.total_price,
                                                     favorites=favorites)

            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            print("no")


    try:
            if request.COOKIES.get("id_user")!='None':
                print("cookie work")
                is_login=True
            else:
                is_login=False
    except:
        is_login=False


    id_user = request.COOKIES.get('id_user')
    products = ProductInBasket.objects.filter(session_key=id_user)
    products_total_nmb=products.count()

    products_in_basket = ProductInBasket.objects.filter(session_key=id_user)

    mtotal_price=0
    for pr in  products_in_basket:
        print(pr.nmb)
        print(pr.product.price)
        pr.total_price=pr.nmb*pr.product.price

        print(pr.total_price)
        mtotal_price+=pr.total_price

    return render(request, 'favorite/checkout.html', locals())