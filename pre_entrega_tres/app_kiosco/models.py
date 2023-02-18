from django.db import models

# Create your models here.

class Provider(models.Model):
    brand = models.CharField(max_length=200)
    def __str__(self):
        return self.brand
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    size = models.IntegerField()
    code = models.IntegerField()
    brand = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}  - {self.size} ML - {self.code}  / {self.brand.brand}'

class Person(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name + ', ' + self.last_name


class Purchase(models.Model):
    amount = models.IntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f'Producto: {self.product.name} - Cantidad: {self.amount} - Cliente: {self.person.name}, {self.person.last_name}'

