from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BillingForm, MakePaymentForm
from .models import BillingAddress, OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    """  """
    form = BillingForm()

    context = {'form': form}

    if request.method == "POST":
        form = BillingForm(request.POST)
        
        if form.is_valid():
            billing_address = form.save(commit=False)
            billing_address.date = timezone.now()
            billing_address.user = request.user
            billing_address.save()
            return redirect('checkout:payment')

    return render(request, 'checkout.html', context)


@login_required()
def payment(request):
    """  """

    if request.method == "POST":
        payment_form = MakePaymentForm(request.POST)
        address_form = BillingAddress.objects.filter(user=request.user)

        if payment_form.is_valid():
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity_and_size in cart.items():
                product = get_object_or_404(Product, pk=id)
                size = quantity_and_size[1]
                quantity = quantity_and_size[0]
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=address_form,
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
                messages.error(request, "You have successfully paid")
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

    return render(request, "payment.html", {'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
