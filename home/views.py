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

# Create your views here.
def index(request):
    return render(request, 'base.html')

def Home(request):
    return render(request, 'home/Home.html')

def recommended_menu(request):
    return render(request, 'home/Recommended_Menu.html')

def promotion(request):
    return render(request, 'home/Promotion.html')