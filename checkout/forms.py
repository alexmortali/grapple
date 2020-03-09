from django import forms
from .models import BillingAddress

class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2040)]

    credit_card_number = forms.CharField(label='Credit card number', required=True)
    cvv = forms.CharField(label='Security code (CVV)', required=True)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=True)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=True)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ('Full_Name', 'Address_Line_1', 'Address_Line_2', 'town_or_City', 'county', 'country', 'postcode')