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
from django.db import transaction
from django.db import connection
from order.models import *

import json
import re

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
        sweet = get_object_or_404(Sweet, pk=pk)
        data = dict()
        data['sweets'] = model_to_dict(sweet)
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
        additionalitem = get_object_or_404(AdditionalItems, pk=pk)
        data = dict()
        data['additionalitems'] = model_to_dict(additionalitem)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response

#------------------------------------------------------------------------------#
class OrdersList(View):
    def get(self, request):
        orders = list(Orders.objects.order_by('order_no').all().values())
        data = dict()
        data['orders'] = orders

        return JsonResponse(data)

class OrdersDetail(View):
    def get(self, request, pk, pk2):

        order_no = pk + '/' + pk2

        order = list(Orders.objects.select_related('id_user')
            .filter(order_no=order_no)
            .values('order_no', 'id_user', 'date', 'total_price', 'payment_method'
            , 'received', 'change'))
        orderlineitem = list(OrderLineItem.objects.select_related('menu_id')
            .filter(order_no=order_no)
            .values('order_no', 'menu_id', 'type', 'sweet_level', 'amount'
            , ))

        data = dict()
        data['order'] = order
        data['orderlineitem'] = orderlineitem

        return JsonResponse(data)

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

class OrderLineItemForm(forms.ModelForm):
    class Meta:
        model = OrderLineItem
        fields = '__all__'

@method_decorator(csrf_exempt, name='dispatch')
class OrdersCreate(View):

    @transaction.atomic
    def post(self, request):
        if Orders.objects.count() != 0:        # Check Number of Record of Invoice Table == SELECT COUNT(*) FROM invoice
            order_no_max = Orders.objects.aggregate(Max('order_no'))['order_no__max']    # SELECT MAX(invoice_no) FROM invoice
            order_no_temp = [re.findall(r'(\w+?)(\d+)', order_no_max)[0]][0]                # Split 'IN100/22' to 'IN' , '100'
            next_order_no = order_no_temp[0] + str(int(order_no_temp[1])+1) + "/22"       # next_invoice_no = 'IN' + '101' + '/22' = 'IN101/22'
        else:
            next_order_no = "IN100/22"        # If Number of Record of Invoice = 0 , next_invoice_no = IN100/22
        print(next_order_no)
        # Copy POST data and correct data type Ex 1,000.00 -> 1000.00
        request.POST = request.POST.copy()
        request.POST['order_no'] = next_order_no
        request.POST['date'] = reFormatDateMMDDYYYY(request.POST['date'])
        request.POST['id_user'] = reFormatDateMMDDYYYY(request.POST['id_user'])
        request.POST['total_price'] = reFormatNumber(request.POST['total_price'])
        request.POST['received'] = reFormatNumber(request.POST['received'])
        request.POST['change'] = reFormatNumber(request.POST['change'])

        data = dict()
        # Insert correct data to invoice
        form = OrdersForm(request.POST)
        if form.is_valid():
            orders = form.save()
            
            # Delete all invoice_line_item of invoice_no before loop insert new data
            OrderLineItemForm.objects.filter(order_no=next_order_no).delete()

            # Read lineitem from ajax and convert to json dictionary
            dict_lineitem = json.loads(request.POST['lineitem'])

            # Loop replace json data with correct data type Ex 1,000.00 -> 1000.00
            for lineitem in dict_lineitem['lineitem']:
                lineitem['order_no'] = next_order_no
                lineitem['unit_price'] = reFormatNumber(lineitem['unit_price'])
                lineitem['quantity'] = reFormatNumber(lineitem['quantity'])
                lineitem['product_total'] = reFormatNumber(lineitem['product_total'])

                # Insert correct data to invoice_line_item
                formlineitem = OrderLineItemForm(lineitem)
                try:
                    formlineitem.save()
                except :
                    # Check something error to show and rollback transaction both invoice and invoice_line_item table
                    data['error'] = formlineitem.errors
                    print (formlineitem.errors)
                    transaction.set_rollback(True)

            # if insert invoice and invoice_line_item success, return invoice data to caller
            data['orders'] = model_to_dict(orders)
        else:
            # if invoice from is not valid return error message
            data['error'] = form.errors
            print (form.errors)

        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class OrdersUpdate(View):

    @transaction.atomic
    def post(self, request):
        # Get order_no from POST data
        order_no = request.POST['order_no']

        orders = Orders.objects.get(order_no=order_no)
        request.POST = request.POST.copy()
        request.POST['date'] = reFormatDateMMDDYYYY(request.POST['date'])
        request.POST['id_user'] = reFormatDateMMDDYYYY(request.POST['id_user'])
        request.POST['total_price'] = reFormatNumber(request.POST['total_price'])
        request.POST['received'] = reFormatNumber(request.POST['received'])
        request.POST['change'] = reFormatNumber(request.POST['change'])

        data = dict()
        # instance is object that will be udpated
        form = OrdersForm(instance=orders, data=request.POST)
        if form.is_valid():
            orders = form.save()

            OrderLineItemForm.objects.filter(order_no=order_no).delete()

            dict_lineitem = json.loads(request.POST['lineitem'])
            for lineitem in dict_lineitem['lineitem']:
                lineitem['order_no'] = order_no
                lineitem['unit_price'] = reFormatNumber(lineitem['unit_price'])
                lineitem['quantity'] = reFormatNumber(lineitem['quantity'])
                lineitem['product_total'] = reFormatNumber(lineitem['product_total'])
                
                formlineitem = OrderLineItemForm(lineitem)
                if formlineitem.is_valid():
                    formlineitem.save()
                else:
                    data['error'] = form.errors
                    transaction.set_rollback(True)

            data['orders'] = model_to_dict(orders)
        else:
            data['error'] = form.errors
            print (form.errors)

        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class OrdersDelete(View):
    def post(self, request):
        order_no = request.POST["order_no"]

        data = dict()
        orders = Orders.objects.get(order_no=order_no)
        if orders:
            orders.delete()
            OrderLineItemForm.objects.filter(order_no=order_no).delete()
            data['message'] = "Order Deleted!"
        else:
            data['error'] = "Error!"

        return JsonResponse(data)

class OrdersReport(View):
    def get(self, request, pk, pk2):
        order_no = pk + "/" + pk2
        orders = list(Orders.objects.filter(order_no=order_no)
            .values('order_no', 'id_user', 'date'
            , 'total_price', 'payment_method', 'received', 'change'))
        orderslineitem = list(OrderLineItemForm.objects.select_related('menu_id')
            .filter(invoice_no=order_no)
            .values('order_no', 'menu_id', 'type', 'sweet_level', 'amount'))

        data = dict()
        data['orders'] =orders[0]
        data['orderslineitem'] = orderslineitem
        
        return render(request, 'orders/report.html', data)


def reFormatDateMMDDYYYY(ddmmyyyy):
        if (ddmmyyyy == ''):
            return ''
        return ddmmyyyy[3:5] + "/" + ddmmyyyy[:2] + "/" + ddmmyyyy[6:]

def reFormatNumber(str):
        if (str == ''):
            return ''
        return str.replace(",", "")