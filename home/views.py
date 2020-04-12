from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view that displays the index page """
    # render index page
    return render(request, "index.html")


def about(request):
    """ A view that displays the index page """
    # render about page
    return render(request, "about.html")


def contact(request):
    """ A view that displays the index page """
    # render contact page
    return render(request, "contact.html")
