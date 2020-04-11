from django.test import TestCase
from checkout.forms import BillingForm, MakePaymentForm

# Create your tests here.


class TestForms(TestCase):
    def test_make_payment_form_is_valid(self):
        form = MakePaymentForm({"credit_card_number": 4242424242424242,
                                "cvv": 111,
                                "expiry_month": 11,
                                "expiry_year": 2024,
                                "stripe_id": 1})
        self.assertTrue(form.is_valid())

    def test_billing_address_is_valid(self):
        form = BillingForm({"Full_Name": "Test",
                            "country": 'wales',
                            "postcode": 'x1x2x3',
                            "town_or_City": "Newport",
                            "Address_Line_1": "x street",
                            "Address_Line_2": "x place",
                            "county": "Gwent",
                            "date": 2011-11-11})
        self.assertTrue(form.is_valid())

    def test_address_line_1_is_missing(self):
        form = BillingForm({"Full_Name": "Test",
                            "country": 'wales',
                            "postcode": 'x1x2x3',
                            "town_or_City": "Newport",
                            "Address_Line_1": "",
                            "Address_Line_2": "x place",
                            "county": "Gwent",
                            "date": 2011-11-11})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["Address_Line_1"], [u"This field is required."])

    def test_postcode_is_missing(self):
        form = BillingForm({"Full_Name": "Test",
                            "country": 'wales',
                            "postcode": '',
                            "town_or_City": "Newport",
                            "Address_Line_1": "x street",
                            "Address_Line_2": "x place",
                            "county": "Gwent",
                            "date": 2011-11-11})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["postcode"], [u"This field is required."])
