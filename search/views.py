from django.shortcuts import render
from products.models import Product

# Create your views here.

def search_products(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    template = 'list_of_products.html'
    search_request = request.GET['q']
    context = {'products': products,
               'page_title': 'Search Results',
               'search_request': search_request}
    return render(request, template, context)