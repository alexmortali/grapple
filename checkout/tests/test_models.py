from django.test import TestCase
from django.contrib.auth import get_user_model
from checkout.models import OrderLineItem, BillingAddress

# Create your tests here.


class TestCheckoutModels(TestCase):

    def test_can_create_a_order_line_item(self):
        orderlineitem = OrderLineItem(order_id=3,
                                      product_id=1,
                                      quantity=2,
                                      size='Large')
        orderlineitem.save()
        self.assertEqual(orderlineitem.order_id, 3)
        self.assertEqual(orderlineitem.product_id, 1)
        self.assertEqual(orderlineitem.quantity, 2)
        self.assertEqual(orderlineitem.size, 'Large')

    def test_can_create_a_billing_address(self):
        user = get_user_model().objects.create(username='testuser')
        billingadress = BillingAddress(user_id=1,
                                       Full_Name="Test",
                                       country='wales',
                                       postcode='x1x2x3',
                                       town_or_City="Newport",
                                       Address_Line_1="x street",
                                       Address_Line_2="x place",
                                       county="Gwent",
                                       date="2011-11-11")
        billingadress.save()
        self.assertEqual(billingadress.user_id, 1)
        self.assertEqual(billingadress.Full_Name, 'Test')
        self.assertEqual(billingadress.country, 'wales')
        self.assertEqual(billingadress.postcode, 'x1x2x3')
        self.assertEqual(billingadress.town_or_City, 'Newport')
        self.assertEqual(billingadress.Address_Line_1, 'x street')
        self.assertEqual(billingadress.Address_Line_2, 'x place')
        self.assertEqual(billingadress.county, 'Gwent')
        self.assertEqual(billingadress.date, '2011-11-11')
