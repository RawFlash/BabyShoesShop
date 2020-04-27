from django.shortcuts import render
from . import models as loginmodels
from favorite import models
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from favorite import models as FavModels
from products import models as Products
from products.forms import NewProductForm, NewProductImageForm


# Create your views here.

def login(request):
    is_admin = False

    if request.method == 'POST':


        if request.POST.get('is_delete')=="True":


            id_delete_product_in_purchase = request.POST.get('id_product_in_purchase')
            print("Id delete product in purchases: "+str(id_delete_product_in_purchase))
            loginmodels.Product_in_purchase.objects.filter(id = int(id_delete_product_in_purchase)).delete()

            purchases = loginmodels.Purchase.objects.all()

            product_in_purchases = loginmodels.Product_in_purchase.objects.all()

            products = FavModels.Product.objects.all()

            is_admin = True
            responce = render(request, 'login/admin.html', locals())
            responce.set_cookie(key="is_admin", value=True)

            return responce

        elif request.POST.get('is_check')=="True":

            purchase = loginmodels.Purchase.objects.filter(id = request.POST.get('id_purchase')).first()

            if purchase.check == True:
                purchase.check = False
            else:
                purchase.check=True

            purchase.save()

            purchases = loginmodels.Purchase.objects.all()

            product_in_purchases = loginmodels.Product_in_purchase.objects.all()

            products = FavModels.Product.objects.all()

            is_admin = True
            responce = render(request, 'login/admin.html', locals())
            responce.set_cookie(key="is_admin", value=True)

            return responce

        elif request.POST.get('is_add') == "True":
            # Добавление выбранного товара в заказ

            id_product = request.POST.get('id_product')
            id_purchase = request.POST.get('id_purchase')
            count = request.POST.get('count')

            new_product_in_purchase = loginmodels.Product_in_purchase.objects.create(id_product=id_product,
                                                                                     id_purchase=id_purchase,
                                                                                     count=count)
            new_product_in_purchase.save()

            purchases = loginmodels.Purchase.objects.all()

            product_in_purchases = loginmodels.Product_in_purchase.objects.all()

            products = FavModels.Product.objects.all()

            is_admin = True
            responce = render(request, 'login/admin.html', locals())
            responce.set_cookie(key="is_admin", value=True)

            return responce

        else:
            login = request.POST.get('login')
            password = request.POST.get('password')


            if password != "":



                purchases = loginmodels.Purchase.objects.all()

                product_in_purchases = loginmodels.Product_in_purchase.objects.all()

                products = FavModels.Product.objects.all()

                for a in products:
                    print(a.id)


                is_admin=True
                responce = render(request, 'login/admin.html', locals())
                responce.set_cookie(key="is_admin", value=True)

                return responce

        return render(request, 'login/login.html',locals())

    return render(request, 'login/login.html',locals())


def add(request):
    if request.method == 'POST':

        id_purchase = request.POST.get('id_purchase')

        purchase = loginmodels.Purchase.objects.filter(id = id_purchase).first()

        products = FavModels.Product.objects.all()
        is_admin = True
        responce = render(request, 'login/add.html', locals())
        responce.set_cookie(key="is_admin", value=True)

        return responce

    purchases = loginmodels.Purchase.objects.all()

    product_in_purchases = loginmodels.Product_in_purchase.objects.all()

    products = FavModels.Product.objects.all()

    is_admin = True
    responce = render(request, 'login/admin.html', locals())
    responce.set_cookie(key="is_admin", value=True)

    return responce

#Добавление продукта в каталог
def add_product(request):

    if request.method == 'POST':

        form = NewProductForm(request.POST)
        form2 = NewProductImageForm(request.POST,request.FILES)

        if request.POST.get('is_name')=='True':


            if form.is_valid():
                form.save()
                form2 = NewProductImageForm(request.POST, request.FILES)
                is_admin = True
                is_login = True
                is_image = True
                return render(request, 'login/add_product.html', locals())


            #Ошика при вводе названия и описания продукта
            else:
                is_admin=True
                is_login = True
                is_image = False
                form = NewProductForm(request.POST)
                form2 = NewProductImageForm(request.POST, request.FILES)
                return render(request, 'login/add_product.html', locals())


        elif request.POST.get('is_image')=='True':
            form2.is_main=True
            print("Добавляем картинку")
            form2.product = Products.Product.objects.last()
            for i in Products.ProductImage.objects.all():
                print(i.image)
            print(form2.is_valid())
            if form2.is_valid():
                print('сохраняем')
                print('image' in request.FILES)
                if 'image' in request.FILES:
                    form2.image = request.FILES['image']
                    form2.save()
                is_admin = True
                is_login = True
                return redirect('http://127.0.0.1:8000/login/out')

            #Ошибка при выборе изображения продукта
            else:
                is_admin = True
                is_login = True
                is_image = True
                form = NewProductForm(request.POST)
                form2 = NewProductImageForm(request.POST, request.FILES)
                return render(request, 'login/add_product.html', locals())

        """
        Title = request.POST.get('title')
        Description = request.POST.get('description')
        Price = request.POST.get('price')
        Image = request.POTS.get('image')

        Product = Products.Product.objects.create(name=Title,Category = Products.ProductCategory.objects.first(),price = Price,
                                                  description = Description)
        Product.save()

        ProductImage = Products.ProductImage.objects.create(product = Product,image = Image,is_main = True)
        ProductImage.save()





        purchases = loginmodels.Purchase.objects.all()

        product_in_purchases = loginmodels.Product_in_purchase.objects.all()

        products = FavModels.Product.objects.all()

        is_admin=True
        responce = render(request, 'login/admin.html', locals())
        responce.set_cookie(key="is_admin", value=True)

        return responce
        """

    is_admin=True
    is_login = True
    is_image = False
    form = NewProductForm(request.POST)
    form2 = NewProductImageForm(request.POST, request.FILES)

    return render(request, 'login/add_product.html', locals())

def out(request):
    response = redirect('/')
    response.set_cookie("id_user", None)
    return response


