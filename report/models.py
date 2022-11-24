from django.db import models

# Create your models here.
class Data(models.Model):
    key = models.CharField(max_length=10,primary_key=True)
    value = models.CharField(max_length=100)

class Customer(models.Model):
    id_user = models.CharField(max_length=10, primary_key=True)
    username = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    point = models.CharField(max_length=100, null=True, blank=True)
    class Meta:
        db_table = "customer"
        managed = False
    def __str__(self):
        return self.id_user

class Menu(models.Model):
    menu_id = models.CharField(max_length=10,primary_key=True)
    menu_name = models.CharField(max_length=10, null=True)
    price = models.CharField(max_length=10, null=True)
    amount_of_coffee = models.CharField(max_length=20, null=True)
    amount_of_milk = models.CharField(max_length=20, null=True)
    amount_of_chocolate = models.CharField(max_length=20, null=True)
    amount_of_syrup = models.CharField(max_length=20, null=True)
    class Meta:
        db_table = "menu"
        managed = False
    def __str__(self):
        return self.menu_id 

class PaymentMethod(models.Model):
    payment_method = models.CharField(max_length=100,primary_key=True)
    description = models.CharField(max_length=100, null=True)
    class Meta:
        db_table = "payment_method"
        managed = False
    def __str__(self):
        return self.payment_method 

class Stock(models.Model):
    id_stock = models.CharField(max_length=10, primary_key=True)
    date_stock = models.DateField(null=True)
    stock_name = models.CharField(max_length=100 ,null=True)
    amount = models.IntegerField(null=True)
    cost = models.FloatField(null=True, blank=True)
    total_amount = models.IntegerField(null=True)
    total_price = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = "stock"
        managed = False
    def __str__(self):
        return self.id_stock

