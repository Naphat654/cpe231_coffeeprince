"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from report import views as report_views
from order import views as order_views
from home import views as home_views
from form import views as form_views
from login import views as login_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', order_views.index, name='index'),

    path('report/report', report_views.report),
    path('customer/list', order_views.CustomerList.as_view(), name='customer_list'),
    path('customer/detail/<pk>', order_views.CustomerDetail.as_view(), name='customer_detail'),
    path('paymentmethod/list', order_views.PaymentMethodList.as_view(), name='payment_method_list'),
    path('paymentmethod/detail/<pk>', order_views.PaymentMethodDetail.as_view(), name='payment_method_detail'),
    
    path('home', home_views.index, name='index'),
    path('Home', home_views.Home),
    path('RecommendedMenu', home_views.recommended_menu),
    path('Promotion', home_views.promotion),

    path('form', form_views.index, name='index'),
    path('form/Customer', form_views.customer),
    path('form/Menu', form_views.menu),
    path('form/Promotion', form_views.promotion),
    path('form/Dependent', form_views.dependent),
    path('form/PaymentMethod', form_views.paymentmethod),
    
    path('customer/get', form_views.customer),
    path('customer/get/<customer_id>', form_views.CustomerGet.as_view(), name='customer_get'), 
    path('customer/save', form_views.CustomerSave.as_view(), name='customer_save'),   
    path('customer/save2', form_views.CustomerSave2.as_view(), name='customer_save2'), 


    path('paymentmethod1/list', form_views.PaymentMethodList.as_view(), name='payment_method_list'),
    path('paymentmethod/get', form_views.paymentmethod),
    path('paymentmethod/get/<payment_method>', form_views.PaymentMethodGet.as_view(), name='payment_method_get'), 
    path('paymentmethod/save', form_views.PaymentMethodSave.as_view(), name='payment_method_save'),   
    path('paymentmethod/save2', form_views.PaymentMethodSave2.as_view(), name='payment_method_save2'),
    
    path('login/', login_views.loginPage, name='login'),
    path('logout/', login_views.logoutUser, name='logout'),
    path('register/', login_views.registerPage, name='register'),

]
