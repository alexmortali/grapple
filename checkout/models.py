from django.contrib.auth import get_user_model
from django.db import models
from products.models import Product

User = get_user_model()

# Create your models here.
class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Full_Name = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=False)
    town_or_City = models.CharField(max_length=40, blank=False)
    Address_Line_1 = models.CharField(max_length=40, blank=False)
    Address_Line_2 = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=True)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}-{3}-{4}".format(self.id, self.date, self.Full_Name, self.Address_Line_1, self.postcode)

class OrderLineItem(models.Model):
    order = models.ForeignKey(BillingAddress, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)
    size = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)