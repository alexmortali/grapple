from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .forms import BillingForm, MakePaymentForm
from .models import BillingAddress, OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def review(request):
    """ View that renders simple review page """

    return render(request, 'review.html')


@login_required()
def payment(request):
    """ View that renders payment page where users can fill
        in 2 forms to complete their order. """

    if request.method == "POST":
        billing_address_form = BillingForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        with transaction.atomic():
            if billing_address_form.is_valid() and payment_form.is_valid():
                billing_address = billing_address_form.save(commit=False)
                billing_address.date = timezone.now()
                billing_address.user = request.user
                billing_address.save()

                cart = request.session.get('cart', {})
                total = 0
                for id, quantity_or_size in cart.items():
                    product = get_object_or_404(Product, pk=id)
                    size = quantity_or_size[1]
                    quantity = quantity_or_size[0]
                    total += quantity * product.price
                    order_line_item = OrderLineItem(
                        order=billing_address,
                        product=product,
                        quantity=quantity,
                        size=size
                    )
                    order_line_item.save()

                try:
                    customer = stripe.Charge.create(
                        amount=int(total * 100),
                        currency="GBP",
                        description=request.user.email,
                        card=payment_form.cleaned_data['stripe_id'],
                    )
                except stripe.error.CardError:
                    messages.error(request, "Your card was declined!")

                if customer.paid:
                    messages.success(
                        request, "You have successfully paid! Why not check out some more products below.")
                    request.session['cart'] = {}
                    return redirect(reverse('products:list_of_products'))
                else:
                    messages.error(request, "Unable to take payment")
            else:
                print(payment_form.errors)
                messages.error(
                    request, "We were unable to take payment with that card!")
    else:
        payment_form = MakePaymentForm()
        billing_address_form = BillingForm()

    return render(request, "payment.html", {'billing_address_form': billing_address_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
