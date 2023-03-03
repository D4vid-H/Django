#from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth.models import User
import random
from .models import  *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_avatar(request):
    if request.method == 'POST':
        formulario = AvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid:
            u = User.objects.get(username=request.user)
            avatar = Avatar(user = u, image = formulario.cleaned_data['image'])
            avatar.save()
            return render(request, "index.html")
    
    else:
        formulario = AvatarFormulario()
    return render(request, "add_avatar.html", {"form":formulario})
    
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
                avatar = Avatar.objects.get(user_id = usuario.id)
                return render(request, 'index.html', {"mensaje": f"Bienvenido {usr}", "avatar":{avatar.image}})
            else:
                return render(request, 'index.html', {"mensaje": 'Error, datos incorrectos'})
        else:
            return render(request, 'index.html', {"mensaje": 'Error, formulario error'})
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
    if request.method == 'POST':
        formulario = UserEditForm(request.POST)
        if formulario.is_valid:
            info = formulario.cleaned_data

            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.save()

            return render(request, 'index.html')
    
    else:
        formulario = UserEditForm(initial = {'username': usuario.username, 'email': usuario.email})
    
    return render(request, 'edit_user.html', {'formulario':formulario, 'usuario': usuario})

@login_required
def product(request):
    return render(request, 'product.html', {'products': Product.objects.all()})
     
@login_required
def product_update(request, param):
    if request.method == "GET":
        update_prod = Product.objects.get(id=param)  
        return render(request, 'form_product_update.html', {'product': update_prod, 'proveedores':Provider.objects.all()}) 

@login_required
def product_delete(request, param):
    delete_prod = Product.objects.get(id=param)
    delete_prod.delete()
    return render(request, 'form_product.html', {'proveedores':Provider.objects.all(), 'products': Product.objects.all()})

@login_required
def provider_update(request, param):
    if request.method == "GET":
        update_prod = Provider.objects.get(id=param)  
        return render(request, 'form_provider_update.html', {'provider': update_prod, 'providers':Provider.objects.all()}) 

@login_required
def provider_delete(request, param):
    delete_prod = Product.objects.get(id=param)
    delete_prod.delete()
    return render(request, 'form_brand.html', {'providers':Provider.objects.all()})

def form(request, a):
    try:
        match a:
            case 'brand':
                if request.method == "GET":
                    return render(request, 'form_brand.html', {'providers': Provider.objects.all()})
                else:
                    if  request.POST['id']:
                        provider = Provider.objects.filter(id = request.POST['id']).update(brand = request.POST['brand'])
                        return render(request, 'form_brand.html', {'providers':Provider.objects.all()})  
                    else: 
                        Provider.objects.create(brand = request.POST['brand'])
                        return redirect("/product/") 
                         
        match a:
            case 'product':
                if request.method == "GET":
                    return render(request, 'form_product.html', {'providers':Provider.objects.all(), 'products': Product.objects.all()})
                else:
                    if  request.POST['code']:
                        product = Product.objects.filter(code = request.POST['code']).update(name = request.POST['name'].capitalize(), size = request.POST['size'])
                        return render(request, 'form_product.html', {'providers':Provider.objects.all(), 'products': Product.objects.all()})
                    else: 
                        name = request.POST['provider']
                        product = Provider.objects.get(brand = name)
                        Product.objects.create(name = request.POST['name'].capitalize(), size = request.POST['size'], code = random.randrange(0000, 9999), brand_id = product.id)
                        return render(request, 'form_product.html', {'providers':Provider.objects.all(), 'products': Product.objects.all()})
        match a:
            case 'client':
                if request.method == "GET":
                    return render(request, 'form_client.html', {'forms': Create_new_person()})
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
        print("Error_form: ", error)
    return render(request, 'index.html')

def search(request):
    try:
        req_name = request.POST['search']
        uno = Product.objects.filter(name__startswith = req_name)
        return render(request, 'product.html', {'products': uno} )
    
    except Exception as error:
        print("Error_search: ", error)

@login_required
def purchase(request):    
    try:
        if request.method == 'POST':
            req_name = request.POST['client'].split()
            id = req_name[0]
            purch = Purchase.objects.filter(id = id) 
            return render(request, 'purchase.html', {'purchases': purch, 'clients': Person.objects.all()})
        else: 
            return render(request, 'purchase.html', {'clients': Person.objects.all()})
    except Exception as error:
        print("Error_purchase: ", error)
 
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')