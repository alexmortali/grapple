from django.shortcuts import render, get_object_or_404
from .forms import QuantityForm, SizeForm
from .models import Category, Product
# Create your views here.

def list_of_products_by_category(request, category_slug):
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    template = 'list_of_products_by_category.html'
    context = {'categories': categories, 'products': products, 'category': category}
    return render(request, template, context)

def list_of_products(request):
    products = Product.objects.all()
    template = 'list_of_products.html'
    context = {'products': products}
    return render(request, template, context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    template = 'product_detail.html'
    context = {'product': product}
    return render(request, template, context)