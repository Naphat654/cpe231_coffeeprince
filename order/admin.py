from django.contrib import admin

# Register your models here.
from .models import Data
from .models import Customer
from .models import PaymentMethod
from .models import Stock

admin.site.register(Data)
admin.site.register(Customer)
admin.site.register(PaymentMethod)
admin.site.register(Stock)
