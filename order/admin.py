from django.contrib import admin

# Register your models here.
from .models import Data
from .models import Customer
from .models import PaymentMethod
<<<<<<< HEAD
from .models import Menu
=======
>>>>>>> 488b168e64e8633a9e3eb0323a892a521401c92c
from .models import Stock
from .models import OrderLineItem
from .models import Orders
from .models import Sweet
from .models import AdditionalItems

admin.site.register(Data)
admin.site.register(Customer)
admin.site.register(PaymentMethod)
admin.site.register(Stock)
<<<<<<< HEAD
admin.site.register(Menu)
=======
admin.site.register(OrderLineItem)
admin.site.register(Orders)
admin.site.register(Sweet)
admin.site.register(AdditionalItems)
>>>>>>> 488b168e64e8633a9e3eb0323a892a521401c92c
