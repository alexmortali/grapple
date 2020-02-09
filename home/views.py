from django.shortcuts import render

# Create your views here.
def index(request):
    """ A view that displays the index page """
    
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")