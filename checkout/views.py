from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BillingForm
from .models import BillingAddress, OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

# Create your views here.

@login_required()
def checkout(request):
    """  """
    form = BillingForm

    context = {'form': form}

    if request.method == "POST":
        if form.is_valid():
            billing_address = form.save(commit=False)
            billing_address.date = timezone.now()
            billing_address.user = request.user
            billing_address.save()
            return redirect('checkout:payment')

    return render(request, 'checkout.html', context)

@login_required()
def payment(request):

    return render(request, 'payment.html')