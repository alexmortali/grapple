from django.contrib import admin
from .models import BillingAddress, OrderLineItem

# Register your models here.
admin.site.register(BillingAddress)
admin.site.register(OrderLineItem)
