from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Max
from .forms import QuantityForm, SizeForm
from .models import Category, Product
from .helper_functions import *
from .constants import *
from reviews.models import Review
# Create your views here.


def list_of_products_by_category(request, category_slug):
    """ View that returns all products within a selected
        category with a sorting option """

    categories = Category.objects.all()
    template = 'list_of_products_by_category.html'
    page = request.GET.get('page')
    category = get_object_or_404(Category, slug=category_slug)

    context = {'categories': categories,
               'category': category,
               'order_by_choices': ORDER_BY_CHOICES,
               'page': page
               }

    if request.method == "GET":
        products = Product.objects.filter(category=category)
        paginator = Paginator(products, products_per_page)
        products = paginator_function(request, paginator)
        context['products'] = products

        return render(request, template, context)
    # If user has selected a filter option
    elif request.method == "POST":
        # Get Users filter option
        selected_filter = request.POST.get('filter_select')
        products = Product.objects.filter(
            category=category).order_by(selected_filter)
        paginator = Paginator(products, products_per_page)
        products = paginator_function(request, paginator)
        context['products'] = products
        context['selected-filter'] = selected_filter

        return render(request, template, context)


def list_of_products(request):
    """ View that returns all products with an option
        to sort products """

    template = 'list_of_products.html'
    page = request.GET.get('page')

    context = {'page_title': 'All Products',
               'order_by_choices': ORDER_BY_CHOICES,
               'page': page
               }

    if request.method == "GET":
        products = Product.objects.all()
        paginator = Paginator(products, products_per_page)
        products = paginator_function(request, paginator)

        context['products'] = products

        return render(request, template, context)
    # If user has selected a filter option
    elif request.method == "POST":
        # Get Users filter option
        selected_filter = request.POST.get('filter_select')
        products = Product.objects.all().order_by(selected_filter)
        paginator = Paginator(products, products_per_page)
        products = paginator_function(request, paginator)

        context['products'] = products
        context['selected_filter'] = selected_filter

        return render(request, template, context)


def product_detail(request, slug):
    """ View that return a single products page """

    product = get_object_or_404(Product, slug=slug)
    # Get products reviews ordered by latest review
    reviews = Review.objects.filter(product=product).order_by('review_date')
    # Get total reviews for that product
    total_reviews = Review.objects.filter(product=product).count()

    # List to be passes into Average function
    rating_function_list = []

    template = 'product_detail.html'
    context = {'product': product,
               'Quantity': QuantityForm,
               'Size': SizeForm,
               'reviews': reviews,
               'total_reviews': total_reviews}
    if reviews:
        for review in reviews:
            # Append each review rating to rating function list.
            rating_function_list.append(review.rating)

    if rating_function_list:
        # If the list has data run Average function on it to get
        # average rating.
        average_rating = Average(rating_function_list)
        context['average_rating'] = average_rating

    return render(request, template, context)
