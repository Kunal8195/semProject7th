from django.contrib import admin
from .models import Customers, Contact, Customer

# Register your models here.

admin.site.register(Customers)
admin.site.register(Contact)
admin.site.register(Customer)
