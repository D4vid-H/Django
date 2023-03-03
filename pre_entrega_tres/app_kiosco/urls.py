from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.login_user, name = "login"),
    path('', views.index, name = "index"),
    path('edit_user/', views.edit_user, name = "edit_user"),
    path('register/', views.register, name = "register"),
    path('logout/', views.logout_user, name = "logout"),
    path('product/', views.product, name = "product"),
    path('purchase/', views.purchase, name = "purchase"),
    path('about/', views.about, name = "about"),
    path('contact/', views.contact, name = "contact"),
    path('form_brand/', views.form, {'a': 'brand'}, name = "form_brand"),
    path('form_provider_update/<param>/', views.provider_update, name = "form_provider_update"),
    path('form_provider_delete/<param>/', views.provider_delete, name = "form_provider_delete"),
    path('form_product/', views.form, {'a': 'product'} ,name = "form_product"),
    path('form_product_update/<param>/', views.product_update, name = "form_product_update"),
    path('form_product_delete/<param>/', views.product_delete, name = "form_product_delete"),
    path('form_client/', views.form, {'a': 'client'}, name = "form_client"),
    path('form_purchase/', views.form, {'a': 'purchase'}, name = "form_purchase"),
    path('product_search/', views.search, name = "product_search"),
    path('new_letter/', views.new_letter, name = "new_letter"),

]
