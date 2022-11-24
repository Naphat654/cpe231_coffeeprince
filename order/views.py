from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from django.db.models import Max
from django.db import connection
from order.models import *

import json

# Create your views here.
def index(request):
    data = {}
    return render(request, 'order/order.html', data)

class MenuList(View):
    def get(self, request):
        menus = list(Menu.objects.all().values())
        data = dict()
        data['menus'] = menus
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

class CustomerList(View):
    def get(self, request):
        customers = list(Customer.objects.all().values())
        data = dict()
        data['customers'] = customers
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

class CustomerDetail(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        data = dict()
        data['customers'] = model_to_dict(customer)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class PaymentMethodList(View):
    def get(self, request):
        payment_methods = list(PaymentMethod.objects.all().values())
        data = dict()
        data['payment_methods'] = payment_methods
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

class PaymentMethodDetail(View):
    def get(self, request, pk):
        payment_method = get_object_or_404(PaymentMethod, pk=pk)
        data = dict()
        data['payment_methods'] = model_to_dict(payment_method)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

class StockList(View):
    def get(self, request):
        stocks = list(Stock.objects.all().values())
        data = dict()
        data['stock'] = stocks
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

class StockDetail(View):
    def get(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        data = dict()
        data['stocks'] = model_to_dict(stock)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

# class Sweet(models.Model):
#     sweet_level = models.IntegerField(primary_key=True)
#     description = models.CharField(max_length=100, null=True)
#     class Meta:
#         db_table = "sweet"
#         managed = False
#     def __str__(self):
#         return self.sweet_level

#    *Sweet
class SweetList(View):
    def get(self, request):
        sweets = list(Sweet.objects.all().values())
        data = dict()
        data['sweets'] = sweets
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

class SweetDetail(View):
    def get(self, request, pk):
        sweets = get_object_or_404(Sweet, pk=pk)
        data = dict()
        data['sweets'] = model_to_dict(Sweet)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

#    *AdditionalItems
class AdditionalItemsList(View):
    def get(self, request):
        additionalitems = list(AdditionalItems.objects.all().values())
        data = dict()
        data['additionalitems'] = additionalitems
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

class AdditionalItemsDetail(View):
    def get(self, request, pk):
        sweets = get_object_or_404(AdditionalItems, pk=pk)
        data = dict()
        data['additionalitems'] = model_to_dict(AdditionalItems)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


