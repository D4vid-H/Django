#from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
import random
from .models import  *
from .forms import *

# Create your views here.

def measures():
    lista = ['g', 'kg', 'ml', 'l', 'u']
    return lista

def index(request):
    return render(request, 'index.html')
    
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usr = form.cleaned_data.get('username')
            pas = form.cleaned_data.get('password')
            user = authenticate(username=usr, password=pas)
            if user is not None:
                login(request, user)
                usuario = User.objects.get(username=user)
                return render(request, 'index.html', {"mensaje": f"Bienvenido {usr}"})
            else:
                return render(request, 'login.html', {"message": 'Error, datos no encontrados', 'form': form})
        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {"message": 'Error, Datos incorrectos','form':form})
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "index.html", {'mensaje': f"Usuario Creado {username}"})
    else:
        form = UserRegisterForm()
    
    return render(request, 'register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect("/")

def new_letter(request):
    try:
        if request.method == 'POST':
            correo = News_letter.objects.get_or_create(email = request.POST['newletter'])    
            return redirect("/")
        else:
            return redirect("/")
    except Exception as error:
        print("Error_news_letter: ", error) 
        
@login_required
def edit_user(request):
    usuario = request.user
    print(usuario)
    if request.method == 'POST':
        formulario = UserEditForm(request.POST)
        if formulario.is_valid:
            info = formulario
            usuario.email = info['email'].value()
            usuario.password1 = info['password1'].value()
            usuario.password2 = info['password2'].value()
            usuario.first_name = info['first_name'].value()
            usuario.last_name = info['last_name'].value()
            usuario.save()

            return render(request, 'index.html')
    
    else:
        formulario = UserEditForm(initial = {'first_name': usuario.first_name, 'last_name': usuario.last_name, 'email': usuario.email})
    
    return render(request, 'edit_user.html', {'formulario':formulario, 'usuario': usuario})

@login_required(login_url='/login/')
def product(request):
    return render(request, 'product.html', {'products': Product.objects.all()})
     
@login_required
def product_update(request, param):
    if request.method == "GET":
        update_prod = Product.objects.get(id=param)  
        return render(request, 'form_product_update.html', {'product': update_prod, 'proveedores':Provider.objects.all(), 'measures': measures()}) 

@login_required
def product_delete(request, param):
    delete_prod = Product.objects.get(id=param)
    delete_prod.delete()
    return render(request, 'form_product.html', {'proveedores':Provider.objects.all(), 'products': Product.objects.all(), 'measures': measures()})

@login_required
def provider_update(request, param):
    if request.method == "GET":
        update_prod = Provider.objects.get(id=param)
        return render(request, 'form_provider_update.html', {'provider': update_prod, 'providers':Provider.objects.all()})
    else:
        Provider.objects.filter(brand = request.POST['id']).update(brand = request.POST['brand'].capitalize())
        return render(request, 'form_provider_update.html', {'providers':Provider.objects.all()})

@login_required
def provider_delete(request, param):
    delete_prov = Provider.objects.get(id=param)
    delete_prov.delete()
    return render(request, 'form_brand.html', {'providers':Provider.objects.all()})

def form(request, a):
    try:
        match a:
            case 'brand':
                if request.method == "GET":
                    return render(request, 'form_brand.html', {'providers': Provider.objects.all()})
                else:
                    if  'id' in request.POST:
                        provider = Provider.objects.filter(id = request.POST['id']).update(brand = request.POST['brand'].capitalize())
                        return render(request, 'form_brand.html', {'providers':Provider.objects.all()})  
                    else: 
                        Provider.objects.create(brand = request.POST['brand'])
                        return render(request, 'form_brand.html', {'providers':Provider.objects.all()}) 
                         
        match a:
            case 'product':
                if request.method == "GET":                    
                    return render(request, 'form_product.html', {'providers':Provider.objects.all(), 'products': Product.objects.all(), 'measures': measures()})
                else:
                    if  'code' in request.POST:
                        product = Product.objects.filter(code = request.POST['code']).update(name = request.POST['name'].capitalize(), size = request.POST['size'], measure = request.POST['measure'])
                        return render(request, 'form_product.html', {'providers':Provider.objects.all(), 'products': Product.objects.all(), 'measures': measures()})
                    else: 
                        name = request.POST['provider']
                        product = Provider.objects.get(brand = name)
                        Product.objects.create(name = request.POST['name'].capitalize(), size = request.POST['size'], measure = request.POST['measure'], code = random.randrange(0000, 9999), brand_id = product.id)
                        return render(request, 'form_product.html', {'providers':Provider.objects.all(), 'products': Product.objects.all(), 'measures': measures()})
       
        match a:
            case 'purchase':
                if request.method == "GET":
                    return render(request, 'form_purchase.html', {'products': Product.objects.all(), 'client': User.objects.get(username = request.user)})
                else:
                    if request.POST['product'] == 'Productos':
                        return render(request, 'form_purchase.html', {'products': Product.objects.all(), 'client': User.objects.get(username = request.user), 'message': 'Seleccione un producto'})
                    else:
                        prod_name = request.POST['product']
                        prod_obj = Product.objects.get(name = prod_name)
                        pers_name = request.user
                        pers_obj = User.objects.get(username = pers_name)
                        Purchase.objects.create(amount = request.POST['amount'], product_id = prod_obj.id, person_id = pers_obj.id)
                        return redirect("/product/")
    
    except Exception as error:
        print("Error_form: ", error)
    return render(request, 'index.html')

def search(request):
    try:
        req_name = request.POST['search']
        uno = Product.objects.filter(name__startswith = req_name)
        return render(request, 'product.html', {'products': uno} )
    
    except Exception as error:
        print("Error_search: ", error)

@login_required(login_url='/login/')
def purchase(request):    
    try:
        if request.method == 'GET':
            purch = Purchase.objects.filter(person_id = request.user.id)
            return render(request, 'purchase.html', {'purchases': purch})
    except Exception as error:
        print("Error_purchase: ", error)
 
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')