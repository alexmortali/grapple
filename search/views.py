from django.shortcuts import render
from products.models import Product
from products.constants import ORDER_BY_CHOICES

# Create your views here.


def search_products(request):
    """ View that returns search results """

    # Filter the products based on search results
    products = Product.objects.filter(name__icontains=request.GET['q'])

    # Get search request for page title on list of products page.
    search_request = request.GET['q']

    template = 'list_of_products.html'
    context = {'products': products,
               'page_title': 'Search Results',
               'search_request': search_request,
               'order_by_choices': ORDER_BY_CHOICES}
    return render(request, template, context)
