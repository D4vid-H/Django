from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Provider(models.Model):
    brand = models.CharField(max_length=200)
    def __str__(self):
        return self.brand
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    size = models.IntegerField()
    measure = models.CharField(max_length=50)
    code = models.IntegerField()
    brand = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.size} {self.measure}'

class Purchase(models.Model):
    amount = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Producto: {self.product.name} - Cantidad: {self.amount} - Cliente: {self.person.username}, {self.person.last_name}'

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null=True, blank=True)

    """ def __str__(self):
        return f"{self.user} - {self.image}" """

class News_letter(models.Model):
    email = models.EmailField(unique=True)