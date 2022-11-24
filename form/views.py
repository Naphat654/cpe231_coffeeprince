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
    def get(self, request, customer_id):
        customers = list(Customer.objects.filter(customer_id=customer_id).values())
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

############################ MENU ##############################

# Create your views here.
def menu(request):
    menu_code = request.GET.get('menu_code','')
    menus = list(Menu.objects.filter(menu_code = menu_code).values())
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
    def get(self, request, menu_code):
        menus = list(Menu.objects.filter(menu_code = menu_code).values())
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

############################# PROMOTION ##############################

# Create your views here.
def promotion(request):
    promotion_code = request.GET.get('promotion_code','')
    promotions = list(Promotion.objects.filter(promotion_code = promotion_code).values())
    data = dict()
    data['promotions'] = promotions
    
    return render(request, 'form/forms_promotion.html', data)

class PromotionList(View):
    def get(self, request):
        promotions = list(Promotion.objects.all().values())
        data = dict()
        data['promotions'] = promotions
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

class PromotionGet(View):
    def get(self, request, promotion_code):
        promotions = list(Promotion.objects.filter(promotion_code = promotion_code).values())
        data = dict()
        data['promotions'] = promotions
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response        

@method_decorator(csrf_exempt, name='dispatch')
class PromotionSave(View):
    def post(self, request):
        request.POST = request.POST.copy()

        form = PromotionForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            ret = dict()
            ret['result'] = "error"
            return JsonResponse(ret)

        promotions = list(Promotion.objects.all().values())
        data = dict()
        data['promotions'] = promotions
        
        return render(request, 'form/forms_promotion.html', data)

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = '__all__'

@method_decorator(csrf_exempt, name='dispatch')
class PromotionSave2(View):
    def post(self, request):
        request.POST = request.POST.copy()

        form = PromotionForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            ret = dict()
            ret['result'] = "error"
            ret['promotions'] = list()
            return JsonResponse(ret)

        promotions = list(Promotion.objects.all().values())
        data = dict()
        data['promotions'] = promotions
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response
        #return render(request, 'forms_customer.html', data)

########################## EMPLOYEE ############################
# Create your views here.
def employee(request):
    employee_id = request.GET.get('employee_id','')
    employees = list(Employee.objects.filter(employee_id = employee_id).values())
    data = dict()
    data['employees'] = employees
    
    return render(request, 'form/forms_employee.html', data)

class EmployeeList(View):
    def get(self, request):
        employees = list(Employee.objects.all().values())
        data = dict()
        data['employees'] = employees
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

class EmployeeGet(View):
    def get(self, request, employee_id):
        employees = list(Employee.objects.filter(employee_id = employee_id).values())
        data = dict()
        data['employees'] = employees
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response        

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeSave(View):
    def post(self, request):
        request.POST = request.POST.copy()

        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            ret = dict()
            ret['result'] = "error"
            return JsonResponse(ret)

        employees = list(Employee.objects.all().values())
        data = dict()
        data['employees'] = employees
        
        return render(request, 'form/forms_employee.html', data)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeSave2(View):
    def post(self, request):
        request.POST = request.POST.copy()

        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            ret = dict()
            ret['result'] = "error"
            ret['employees'] = list()
            return JsonResponse(ret)

        employees = list(Employee.objects.all().values())
        data = dict()
        data['employees'] = employees
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response
        #return render(request, 'forms_customer.html', data)

############################# DEPENDENT ############################

def dependent(request):
    employee_id = request.GET.get('employee_id','')
    dependents = list(Dependent.objects.filter(employee_id=employee_id).values())
    data = dict()
    data['dependents'] = dependents
    
    return render(request, 'form/forms_dependent.html', data)

class DependentList(View):
    def get(self, request):
        dependents = list(Dependent.objects.all().values())
        data = dict()
        data['dependents'] = dependents
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

class DependentGet(View):
    def get(self, request, employee_id):
        dependents = list(Dependent.objects.filter(employee_id=employee_id).values())
        data = dict()
        data['dependents'] = dependents
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response        

@method_decorator(csrf_exempt, name='dispatch')
class DependentSave(View):
    def post(self, request):
        request.POST = request.POST.copy()

        form = DependentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            ret = dict()
            ret['result'] = "error"
            return JsonResponse(ret)

        dependents = list(Dependent.objects.all().values())
        data = dict()
        data['dependents'] = dependents
        
        return render(request, 'form/forms_dependent.html', data)

class DependentForm(forms.ModelForm):
    class Meta:
        model = Dependent
        fields = '__all__'

@method_decorator(csrf_exempt, name='dispatch')
class DependentSave2(View):
    def post(self, request):
        request.POST = request.POST.copy()

        form = DependentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            ret = dict()
            ret['result'] = "error"
            ret['dependents'] = list()
            return JsonResponse(ret)

        dependents = list(Dependent.objects.all().values())
        data = dict()
        data['dependents'] = dependents
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

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