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
from form.models import *

import json

def index(request):
    return render(request, 'form/base_form.html')

# Create your views here.
def customer(request):
    id_user = request.GET.get('id_user','')
    customers = list(Customer.objects.filter(id_user=id_user).values())
    data = dict()
    data['customers'] = customers
    
    return render(request, 'form/forms_customer.html', data)

class CustomerList(View):
    def get(self, request):
        customers = list(Customer.objects.all().values())
        data = dict()
        data['customers'] = customers
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

class CustomerGet(View):
    def get(self, request, id_user):
        customers = list(Customer.objects.filter(id_user=id_user).values())
        data = dict()
        data['customers'] = customers
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response        

@method_decorator(csrf_exempt, name='dispatch')
class CustomerSave(View):
    def post(self, request):
        request.POST = request.POST.copy()

        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            ret = dict()
            ret['result'] = "error"
            return JsonResponse(ret)

        customers = list(Customer.objects.all().values())
        data = dict()
        data['customers'] = customers
        
        return render(request, 'form/forms_customer.html', data)

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

@method_decorator(csrf_exempt, name='dispatch')
class CustomerSave2(View):
    def post(self, request):
        request.POST = request.POST.copy()

        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            ret = dict()
            ret['result'] = "error"
            ret['customers'] = list()
            return JsonResponse(ret)

        customers = list(Customer.objects.all().values())
        data = dict()
        data['customers'] = customers
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response
        #return render(request, 'forms_customer.html', data)

############################# Stock ##############################

# Create your views here.
def stock(request):
    id_stock = request.GET.get('id_stock','')
    stocks = list(Stock.objects.filter(id_stock = id_stock).values())
    data = dict()
    data['stocks'] = stocks
    
    return render(request, 'form/forms_stock.html', data)

class StockList(View):
    def get(self, request):
        stocks = list(Stock.objects.all().values())
        data = dict()
        data['stocks'] = stocks
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

class StockGet(View):
    def get(self, request, id_stock):
        stocks = list(Stock.objects.filter(id_stock = id_stock).values())
        data = dict()
        data['stocks'] = stocks
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response        

@method_decorator(csrf_exempt, name='dispatch')
class StockSave(View):
    def post(self, request):
        request.POST = request.POST.copy()

        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            ret = dict()
            ret['result'] = "error"
            return JsonResponse(ret)

        stocks = list(Stock.objects.all().values())
        data = dict()
        data['stocks'] = stocks
        
        return render(request, 'form/forms_stock.html', data)

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'

@method_decorator(csrf_exempt, name='dispatch')
class StockSave2(View):
    def post(self, request):
        request.POST = request.POST.copy()

        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            ret = dict()
            ret['result'] = "error"
            ret['stocks'] = list()
            return JsonResponse(ret)

        stocks = list(Stock.objects.all().values())
        data = dict()
        data['stocks'] = stocks
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response
        #return render(request, 'forms_customer.html', data)

############################ INGREDIENT ########################

############################ MENU ##############################

# Create your views here.
def menu(request):
    menu_id = request.GET.get('menu_id','')
    menus = list(Menu.objects.filter(menu_id = menu_id).values())
    data = dict()
    data['menus'] = menus
    
    return render(request, 'form/forms_menu.html', data)

class MenuList(View):
    def get(self, request):
        menus = list(Menu.objects.all().values())
        data = dict()
        data['menus'] = menus
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

class MenuGet(View):
    def get(self, request, menu_id):
        menus = list(Menu.objects.filter(menu_id = menu_id).values())
        data = dict()
        data['menus'] = menus
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response        

@method_decorator(csrf_exempt, name='dispatch')
class MenuSave(View):
    def post(self, request):
        request.POST = request.POST.copy()

        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            ret = dict()
            ret['result'] = "error"
            return JsonResponse(ret)

        menus = list(Menu.objects.all().values())
        data = dict()
        data['menus'] = menus
        
        return render(request, 'form/forms_menu.html', data)

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

@method_decorator(csrf_exempt, name='dispatch')
class MenuSave2(View):
    def post(self, request):
        request.POST = request.POST.copy()

        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            ret = dict()
            ret['result'] = "error"
            ret['menus'] = list()
            return JsonResponse(ret)

        menus = list(Menu.objects.all().values())
        data = dict()
        data['menus'] = menus
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response
        #return render(request, 'forms_customer.html', data)



###################### PAYMENTMETHOD ###########################

def paymentmethod(request):
    payment_method = request.GET.get('payment_method','')
    paymentmethods = list(PaymentMethod.objects.filter(payment_method=payment_method).values())
    data = dict()
    data['paymentmethods'] = paymentmethods
    
    return render(request, 'form/forms_paymentmethod.html', data)

class PaymentMethodList(View):
    def get(self, request):
        paymentmethods = list(PaymentMethod.objects.all().values())
        data = dict()
        data['paymentmethods'] = paymentmethods
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

class PaymentMethodGet(View):
    def get(self, request, payment_method):
        paymentmethods = list(PaymentMethod.objects.filter(payment_method=payment_method).values())
        data = dict()
        data['paymentmethods'] = paymentmethods
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response        

@method_decorator(csrf_exempt, name='dispatch')
class PaymentMethodSave(View):
    def post(self, request):
        request.POST = request.POST.copy()

        form = PaymentMethodForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            ret = dict()
            ret['result'] = "error"
            return JsonResponse(ret)

        paymentmethods = list(PaymentMethod.objects.all().values())
        data = dict()
        data['paymentmethods'] = paymentmethods
        
        return render(request, 'form/forms_paymentmethod.html', data)

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

@method_decorator(csrf_exempt, name='dispatch')
class PaymentMethodSave2(View):
    def post(self, request):
        request.POST = request.POST.copy()

        form = PaymentMethodForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            ret = dict()
            ret['result'] = "error"
            ret['paymentmethods'] = list()
            return JsonResponse(ret)

        paymentmethods = list(PaymentMethod.objects.all().values())
        data = dict()
        data['paymentmethods'] = paymentmethods
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response