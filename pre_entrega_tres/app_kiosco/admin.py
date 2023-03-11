from django.contrib import admin
from .models import *

# Register your models here.

lista = [Provider, Product, Purchase, Avatar]

admin.site.register(lista)