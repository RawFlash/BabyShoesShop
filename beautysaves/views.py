from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import GirlsForm
from products.models import *
from favorite import models as FavModels
from login import models as loginmodels
import datetime
import requests

def beautysaves(request):
    form = GirlsForm(request.POST or None)
    if request.method == "POST":
        print(form)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])
        if form.is_valid():
            form2=form.save()
    #is_login = request{""}
    print(request)
    print(type(request))

    try:
            if request.COOKIES.get("id_user")!='None':
                print("cookie work")
                is_login=True
            else:
                is_login=False
    except:
        is_login=False

    id_user = request.COOKIES.get('id_user')
    products = FavModels.ProductInBasket.objects.filter(session_key=id_user)
    products_total_nmb=products.count()

    return render(request,'beautysaves/beautysaves.html', locals())


def home(request):


    #TEST

    products = Product.objects.all()

    products_images = ProductImage.objects.all()


    if request.COOKIES.get("id_user") != None and request.COOKIES.get("id_user") !="None" :
        #print("cookie work")

        id_user = request.COOKIES.get('id_user')
        is_login=True
    else:
        # New user

        NewUser = loginmodels.LoginUser.objects.create(login=str(datetime.datetime.now()), password="",
                                                       favorite=FavModels.Favorite.objects.create(status_id=1))

        NewUser.save()
        id_user = loginmodels.LoginUser.objects.all().last().id

        is_login=True

    products = FavModels.ProductInBasket.objects.filter(session_key=id_user)
    products_total_nmb=products.count()

    is_admin = False

    responce = render(request,'beautysaves/home.html', locals())
    responce.set_cookie(key="id_user",value=id_user)
    responce.set_cookie(key="is_admin", value=False)


    return responce

def buy(request):

    if request.method == 'POST':

        #Пользователь оформил покупку

        #Надо перенести все данные в покупку

        id_user = request.COOKIES.get('id_user')
        name = request.POST.get('name')
        address = request.POST.get('address')
        if request.POST.get('pay') == 'cash':
            cash = True
        else:
            cash = False

        Purchase = loginmodels.Purchase.objects.create(name = name,address = address, cash = cash)
        Purchase.save()
        zakaz = int(Purchase.id)

        productsinbasket = FavModels.ProductInBasket.objects.filter(session_key=id_user)

        for product in productsinbasket:
            new_product = loginmodels.Product_in_purchase.objects.create(id_product = product.product_id,
                                                                        id_purchase =  loginmodels.Purchase.objects.all().last().id,
                                                                         count = product.nmb)
            new_product.save()

        #Надо удалить все объекты из корзины пользователя
        FavModels.ProductInBasket.objects.all().delete()


        responce = render(request, 'beautysaves/home.html', locals())
        print("pzdc")

        is_admin = False
        is_login = True

        if cash == False:
            return render(request, 'login/payment.html', locals())

        return render(request,"login/end_buy.html", locals())

    else:
        is_admin=False
        is_login=True

        id_user = request.COOKIES.get('id_user')

        products = FavModels.ProductInBasket.objects.filter(session_key=id_user)
        products_total_nmb = products.count()

        responce = render(request, 'login/buy.html', locals())
        return render(request, 'login/buy.html', locals())

def end_buy(request):
    if request.POST.get('go_to_main') == 'True':
        is_admin = False
        is_login = True

        return  redirect('http://127.0.0.1:8000',locals())
    zakaz = request.POST.get('zakaz')
    is_admin = False
    is_login = True
    return render(request, 'login/end_buy.html', locals())



