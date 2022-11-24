from django.contrib import admin

# Register your models here.
from .models import Data
from .models import Customer
from .models import PaymentMethod
<<<<<<< HEAD
from .models import Menu

=======
from .models import Stock

admin.site.register(Data)
>>>>>>> 33b98b1358fa2be4377ddde7a9d3e053e3925125
admin.site.register(Customer)
admin.site.register(PaymentMethod)
admin.site.register(Stock)
