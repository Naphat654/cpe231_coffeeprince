from django.contrib import admin

# Register your models here.
from .models import Data
from .models import Customer
from .models import PaymentMethod
from .models import Menu
from .models import Stock
from .models import Ingredient
from .models import OrderLineItem
from .models import Orders
from .models import Sweet
from .models import AdditionalItems

admin.site.register(Data)
admin.site.register(Customer)
admin.site.register(PaymentMethod)
admin.site.register(Stock)
admin.site.register(Ingredient)
admin.site.register(Menu)
admin.site.register(OrderLineItem)
admin.site.register(Orders)
admin.site.register(Sweet)
admin.site.register(AdditionalItems)
