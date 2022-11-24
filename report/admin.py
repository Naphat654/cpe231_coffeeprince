from django.contrib import admin

# Register your models here.
from report.models import Data

admin.site.register(Data)

from .models import Menu
from .models import Customer
from .models import PaymentMethod
from .models import Stock

admin.site.register(Menu)
admin.site.register(Customer)
admin.site.register(PaymentMethod)
admin.site.register(Stock)
