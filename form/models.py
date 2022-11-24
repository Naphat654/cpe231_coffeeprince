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
    menu_name = models.CharField(max_length=20, null=True)
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
    description = models.CharField(max_length=100, null=True, blank=True)
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
    
class Ingredient(models.Model):
    id_stock = models.ForeignKey(Stock, on_delete=models.CASCADE, db_column='id_stock')
    ingredient = models.CharField(max_length=100)
    remain = models.IntegerField(null=True)
    class Meta:
        db_table = "ingredient"
        managed = False
    def __str__(self):
        return self.id_stock

class AdditionalItems(models.Model):
    type = models.CharField(max_length=10, primary_key=True)
    description = models.CharField(max_length=100, null=True)
    mash = models.IntegerField(null=True)
    class Meta:
        db_table = "additional_items"
        managed = False
    def __str__(self):
        return self.type

class Sweet(models.Model):
    sweet_level = models.CharField(max_length=10, primary_key=True)
    description = models.CharField(max_length=100, null=True)
    class Meta:
        db_table = "sweet"
        managed = False
    def __str__(self):
        return self.sweet_level

class Orders(models.Model):
    order_no = models.CharField(max_length=10, primary_key=True)
    id_user = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='id_user')
    date = models.DateField(null=True)
    total_price = models.FloatField(null=True, blank=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, db_column='payment_method')
    received = models.FloatField(null=True, blank=True)
    change = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = "orders"
        managed = False
    def __str__(self):
        return "%s %s" % (self.order_no, self.date)              

class OrderLineItem(models.Model):
    order_no = models.ForeignKey(Orders, on_delete=models.CASCADE, db_column='order_no')
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE, db_column='menu_id')
    type = models.ForeignKey(AdditionalItems, on_delete=models.CASCADE, db_column='type')
    sweet_level = models.ForeignKey(Sweet, on_delete=models.CASCADE, db_column='sweet_level')
    amount = models.IntegerField(null=True)
    class Meta:
        db_table = "order_line_item"
        unique_together = (("order_no", "menu_id"),)
        managed = False
    def __str__(self):
        return '{"order_no":"%s","menu_id":"%s","type":"%s","sweet_level":"%s","amount":%s}' % (self.order_no, self.menu_id, self.type, self.sweet_level, self.amount)        
