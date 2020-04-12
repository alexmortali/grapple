from django import forms
from products.constants import SIZE_CHOICES


class QuantityForm(forms.Form):
    """ Form for user to select quantity """

    quantity = forms.IntegerField(min_value=1, max_value=10, widget=forms.Select(
        choices=[(i, i) for i in range(1, 11)]))


class SizeForm(forms.Form):
    """ Form for user to select size """

    size = forms.CharField(required=True, widget=forms.Select(
        choices=SIZE_CHOICES))
