#from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import  *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def product(request):
    return render(request, 'product.html', {'products': Product.objects.all()} )

def form(request, a):
    try:
        match a:
            case 'brand':
                if request.method == "GET":
                    return render(request, 'form_brand.html')
                else:
                    print("Prueba Db add")
                    Provider.objects.create(brand = request.POST['brand'])
                    return redirect("/product/")    
        match a:
            case 'product':
                if request.method == "GET":
                    return render(request, 'form_product.html', {'proveedores':Provider.objects.all()})
                else:
                    name = request.POST['provider']
                    product = Provider.objects.get(brand = name)
                    Product.objects.create(name = request.POST['name'], size = request.POST['size'], code = request.POST['code'], brand_id = product.id)
                    return redirect("/product/")
        match a:
            case 'client':
                if request.method == "GET":
                    return render(request, 'form_client.html', {'form': Create_new_person()})
                else:
                    print("Prueba Db add Person")
                    Person.objects.create(name = request.POST['name'], last_name = request.POST['last_name'])
                    return redirect("/product/")
        match a:
            case 'purchase':
                if request.method == "GET":
                    return render(request, 'form_purchase.html', {'products': Product.objects.all(), 'clients': Person.objects.all()})
                else:
                    print("Prueba Db add compra")
                    prod_name = request.POST['product']
                    prod_obj = Product.objects.get(name = prod_name)
                    print(prod_obj.id)
                    pers_name = request.POST['client']
                    pers_obj = Person.objects.get(name = pers_name)
                    print(pers_obj.id)
                    Purchase.objects.create(amount = request.POST['amount'], product_id = prod_obj.id, person_id = pers_obj.id)
                    return redirect("/product/")
    
    except Exception as error:
        print("Error: ", error)
    return render(request, 'form.html')

def search(request):
    try:

        req_name = request.POST['search']
        uno = []
        uno.append(Product.objects.get(name = req_name))
        return render(request, 'product.html', {'products': uno} )
    
    except Exception as error:
        print("Error: ", error)

def purchase(request):
    return render(request, 'purchase.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')