from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import PaymentMethod
from .models import Menu


admin.site.register(Customer)
admin.site.register(PaymentMethod)
admin.site.register(Menu)