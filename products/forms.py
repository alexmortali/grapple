from django import forms

SIZE_CHOICES = (
    ("Extra Small", "XS"),
    ('Small', 'S'),
    ('Medium', 'M'),
    ('Large', 'L'),
    ('Extra Large', 'XL')
)


class QuantityForm(forms.Form):
    """ Form for user to select quantity """

    quantity = forms.IntegerField(min_value=1, max_value=10, widget=forms.Select(
        choices=[(i, i) for i in range(1, 11)]))


class SizeForm(forms.Form):
    """ Form for user to select size """

    size = forms.CharField(max_length=100, required=True, widget=forms.Select(
        choices=SIZE_CHOICES))
