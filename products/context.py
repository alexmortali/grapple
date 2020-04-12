from products.models import Category


def category_list(request):
    """ Returns categories for Navbar """

    categories = Category.objects.all()
    return {'categories': categories}
