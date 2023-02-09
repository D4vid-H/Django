from django.db import models

# Create your models here.

class Provider(models.Model):
    brand = models.CharField(max_length=200)
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    size = models.IntegerField()
    code = models.IntegerField()
    product = models.ForeignKey(Provider, on_delete=models.CASCADE)

class Person(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=200)

class Purchase(models.Model):
    amount = models.IntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


