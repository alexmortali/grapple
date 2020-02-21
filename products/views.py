from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .forms import QuantityForm, SizeForm
from .models import Category, Product
# Create your views here.

def all_products(request):
    products = Product.objects.all()
    return render(request, "categories.html", {"products": products, "category": "All Products"})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "product_detail.html", {"product": product})
