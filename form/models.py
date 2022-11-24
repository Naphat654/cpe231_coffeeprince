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
    menu_code = models.CharField(max_length=50,primary_key=True)
    unit_price = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = "menu"
        managed = False
    def __str__(self):
        return self.menu_code 

class PaymentMethod(models.Model):
    payment_method = models.CharField(max_length=100,primary_key=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    class Meta:
        db_table = "payment_method"
        managed = False
    def __str__(self):
        return self.payment_method 

class Promotion(models.Model):
    promotion_code = models.CharField(max_length=50, primary_key=True)
    description = models.CharField(max_length=100 ,null=True)
    discount = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = "promotion"
        managed = False
    def __str__(self):
        return self.promotion_code
    
class Employee(models.Model):
    employee_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=10, null=True)
    class Meta:
        db_table = "employee"
        managed = False
    def __str__(self):
        return self.employee_id
    
class Dependent(models.Model):
    employee_id = models.ForeignKey(Employee, primary_key=True, on_delete=models.CASCADE, db_column='employee_id')
    name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=10, null=True)
    relationship = models.CharField(max_length=50, null=True)
    class Meta:
        db_table = "dependent"
        managed = False
    def __str__(self):
        return self.employee_id

class Order(models.Model):
    order_no = models.CharField(max_length=10, primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='customer_id')
    date = models.DateField(null=True)
    total = models.FloatField(null=True, blank=True)
    promotion_code = models.ForeignKey(Promotion, on_delete=models.CASCADE, db_column='promotion_code')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, db_column='payment_method')
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='employee_id')
    rebate = models.FloatField(null=True, blank=True)
    remain = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = "order1"
        managed = False
    def __str__(self):
        return "%s %s" % (self.order_no, self.date)              

class OrderLineItem(models.Model):
    order_no = models.ForeignKey(Order, primary_key=True, on_delete=models.CASCADE, db_column='order_no')
    item_no = models.IntegerField()
    menu_code = models.CharField(max_length=50)
    unit_price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    product_total = models.FloatField(null=True)
    class Meta:
        db_table = "order_lineitem"
        unique_together = (("order_no", "item_no"),)
        managed = False
    def __str__(self):
        return '{"order_no":"%s","item_no":"%s","menu_code":"%s","unit_price":"%s","quantity":%s."Product_total":%s}' % (self.order_no, self.item_no, self.menu_code, self.unit_price, self.quantity,self.product_total)        