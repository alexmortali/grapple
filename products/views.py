from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Max
from .forms import QuantityForm, SizeForm
from .models import Category, Product
from reviews.models import Review
# Create your views here.

ORDER_BY_CHOICES = (
    ('pk', 'Sort:'),
    ('price', 'Price: Low to High'),
    ('-price', 'Price: High to Low'),
    ('name', 'Name: A to Z'),
    ('-name', 'Name: Z to A'),
)


def list_of_products_by_category(request, category_slug):
    """ View that returns all products within a selected
        category with a sorting option """

    categories = Category.objects.all()
    template = 'list_of_products_by_category.html'

    if request.method == "GET":
        products = Product.objects.all()
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
            paginator = Paginator(products, 1)
            page = request.GET.get('page')
            try:
                products = paginator.page(page)
            except PageNotAnInteger:
                products = paginator.page(1)
            except EmptyPage:
                products = paginator.page(paginator.num_pages)

        context = {'categories': categories,
                   'products': products,
                   'category': category,
                   'order_by_choices': ORDER_BY_CHOICES,
                   'page': page
                   }
        return render(request, template, context)
    if request.method == "POST":
        selected = request.POST.get('filter_select')
        products = Product.objects.all().order_by(selected)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category).order_by(selected)
            paginator = Paginator(products, 1)
            page = request.GET.get('page')
            try:
                products = paginator.page(page)
            except PageNotAnInteger:
                products = paginator.page(1)
            except EmptyPage:
                products = paginator.page(paginator.num_pages)
        context = {'categories': categories,
                   'products': products,
                   'category': category,
                   'order_by_choices': ORDER_BY_CHOICES,
                   'selected-filter': selected,
                   'page': page
                   }
        return render(request, template, context)


def list_of_products(request):
    """ View that returns all products with an option
        to sort products """

    template = 'list_of_products.html'

    if request.method == "GET":
        products = Product.objects.all()
        paginator = Paginator(products, 2)
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context = {'products': products,
                   'page_title': 'All Products',
                   'order_by_choices': ORDER_BY_CHOICES,
                   'page': page
                   }
        return render(request, template, context)
    elif request.method == "POST":
        selected = request.POST.get('filter_select')
        products = Product.objects.all().order_by(selected)
        paginator = Paginator(products, 2)
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context = {'products': products,
                   'page_title': 'All Products',
                   'order_by_choices': ORDER_BY_CHOICES,
                   'page': page
                   }
        return render(request, template, context)


def Average(list):
    return sum(list) / len(list)


def product_detail(request, slug):
    """ View that return a single products page """

    product = get_object_or_404(Product, slug=slug)
    reviews = Review.objects.filter(product=product).order_by('review_date')
    total_reviews = Review.objects.filter(product=product).count()
    rating_function_list = []

    context = {'product': product,
               'Quantity': QuantityForm,
               'Size': SizeForm,
               'reviews': reviews,
               'total_reviews': total_reviews}
    
    if reviews:
        for review in reviews:
            rating_function_list.append(review.rating)

    if rating_function_list:
        average_rating = round(Average(rating_function_list), 1)
        context['average_rating'] = average_rating

    
    template = 'product_detail.html'
    
    return render(request, template, context)
