from django.contrib import admin
from .models import *

# Register your models here.

lista = [Provider, Product, Person, Purchase]

admin.site.register(lista)