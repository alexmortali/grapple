from django.shortcuts import render
from products.models import Category

# Create your views here.
def index(request):
    """ A view that displays the index page """
    return render(request, "index.html")

def about(request):
    """ A view that displays the index page """
    return render(request, "about.html")

def contact(request):
    """ A view that displays the index page """
    return render(request, "contact.html")