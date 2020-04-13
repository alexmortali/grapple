from django.shortcuts import render
from products.models import Product
from reviews.models import Review
from checkout.models import OrderLineItem
from products.helper_functions import Average
# Create your views here.


def index(request):
    """ A view that displays the index page """
    # render index page
    return render(request, "index.html")


def about(request):
    """ A view that displays the about page.
    With variables for the count section. """

    total_products = Product.objects.all().count()
    total_orders = OrderLineItem.objects.all().count()
    reviews = Review.objects.all()

    rating_function_list = []
    review_percentage = 0

    if reviews:
        for review in reviews:
            # Append each review rating to rating function list.
            rating_function_list.append(review.rating)

    if rating_function_list:
        # If the list has data run Average function on it to get
        # average rating.
        average_rating = Average(rating_function_list)
        review_percentage = average_rating * 20
    else:
        review_percentage = 100

    context = {'total_products': total_products,
               'total_orders': total_orders,
               'review_percentage': review_percentage
               }

    template = "about.html"
    return render(request, template, context)


def contact(request):
    """ A view that displays the contact page """
    # render contact page
    return render(request, "contact.html")
