from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('product/', views.product, name = "product"),
    path('purchase/', views.purchase, name = "purchase"),
    path('about/', views.about, name = "about"),
    path('contact/', views.contact, name = "contact"),
    path('form_brand/', views.form, {'a': 'brand'},name = "form_brand"),
    path('form_product/', views.form, {'a': 'product'} ,name = "form_product"),
    path('form_client/', views.form, {'a': 'client'}, name = "form_client"),
    path('form_purchase/', views.form, {'a': 'purchase'}, name = "form_purchase"),
    path('product_search/', views.search, name = "product_search"),

]
