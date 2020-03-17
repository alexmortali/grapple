from django.shortcuts import render, get_object_or_404
from django.db.models import Max
from .forms import QuantityForm, SizeForm
from .models import Category, Product
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

    if request.method == "GET":
        products = Product.objects.all()
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        template = 'list_of_products_by_category.html'
        context = {'categories': categories,
                   'products': products,
                   'category': category,
                   'order_by_choices': ORDER_BY_CHOICES
                   }
        return render(request, template, context)
    if request.method == "POST":
        selected = request.POST.get('filter_select')
        products = Product.objects.all().order_by(selected)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category).order_by(selected)
        template = 'list_of_products_by_category.html'
        context = {'categories': categories,
                   'products': products,
                   'category': category,
                   'order_by_choices': ORDER_BY_CHOICES,
                   'selected-filter': selected
                   }
        return render(request, template, context)


def list_of_products(request):
    """ View that returns all products with an option
        to sort products """

    if request.method == "GET":
        products = Product.objects.all()
        template = 'list_of_products.html'
        context = {'products': products,
                   'page_title': 'All Products',
                   'order_by_choices': ORDER_BY_CHOICES
                   }
        return render(request, template, context)
    elif request.method == "POST":
        selected = request.POST.get('filter_select')
        products = Product.objects.all().order_by(selected)
        template = 'list_of_products.html'
        context = {'products': products,
                   'page_title': 'All Products',
                   'order_by_choices': ORDER_BY_CHOICES
                   }
        return render(request, template, context)


def product_detail(request, slug):
    """ View that return a single products page """

    product = get_object_or_404(Product, slug=slug)
    template = 'product_detail.html'
    context = {'product': product,
               'Quantity': QuantityForm,
               'Size': SizeForm}
    return render(request, template, context)
