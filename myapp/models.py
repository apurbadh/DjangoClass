from django.db import models

# Create your models here.

class Shop(models.Model):
    shop_name = models.CharField(max_length=255)
    contact = models.BigIntegerField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
    def __str__(self):
        return self.shop_name
    

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    discount = models.FloatField()
    old_price = models.IntegerField()
    image = models.ImageField(upload_to="myapp/", null=True)
    
    def __str__(self) -> str:
        return self.product_name

class Deal(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    deal_name = models.CharField(max_length=255)
    valid_from = models.DateField()
    valid_till = models.DateField()
    discount_percent = models.FloatField()
    image = models.ImageField(upload_to="myapp/", null=True)
    
    def __str__(self) -> str:
        return self.deal_name
    
    


     
