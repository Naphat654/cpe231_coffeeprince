from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.http import JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import connection
from report.models import *
import json
import datetime

# Create your views here.

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [name[0].replace(" ", "_").lower() for name in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def CursorToDict(data,columns):
    result = []
    fieldnames = [name.replace(" ", "_").lower() for name in columns]
    for row in data:
        rowset = []
        for field in zip(fieldnames, row):
            rowset.append(field)
        result.append(dict(rowset))
    return result

def reFormatDateMMDDYYYY(ddmmyyyy):
        if (ddmmyyyy == ''):
            return ''
        return ddmmyyyy[0:4] + "/" + ddmmyyyy[5:7] + "/" + ddmmyyyy[8:10]
    
def report(request):
    date1 = request.GET.get('date1','')
    date1 = reFormatDateMMDDYYYY(date1)
    date2 = request.GET.get('date2','')
    date2 = reFormatDateMMDDYYYY(date2)

    if date1 == '':
        date1 = str(datetime.datetime.now().date())
    if date2 == '':
        date2 = str(datetime.datetime.now().date())
    with connection.cursor() as cursor:
        cursor.execute (' SELECT m.menu_name as "Menu Name", '
                                ' o.total_price as "Unit Price", ol.amount as "Quantity", '
                                ' (ol.unit_price)*SUM(ol.quantity) as "Total" '
                                ' FROM order_line_item as ol JOIN orders as o ON o.order_no = ol.order_no'
                                ' JOIN menu as m ON m.menu_id = ol.menu_id'
                                " WHERE o.date BETWEEN '{}' AND '{}' "
                                ' GROUP BY ol.menu_name, ol.total_price'.format(str(date1),str(date2)))
        row = dictfetchall(cursor)
        column_name = [col[0] for col in cursor.description]

        cursor.execute ('SELECT SUM(o.total_price) as "Total" '
                                ' FROM orders as o '
                                " WHERE o.date BETWEEN '{}' AND '{}' ".format(str(date1),str(date2)))
        row2 = dictfetchall(cursor)
        column_name2 = [col[0] for col in cursor.description]

    data_report = dict()
    data_report['data'] = row
    data_report['column_name'] = column_name
    data_report['data2'] = row2
    data_report['column_name2'] = column_name2
    return render(request, 'report/report.html', data_report)