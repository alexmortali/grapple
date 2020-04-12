from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginator_function(request, paginator):
    """ Paginator function returning correct products """
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
        return products
    except PageNotAnInteger:
        products = paginator.page(1)
        return products
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        return products


def Average(list):
    """ Helper function to return an average a list """

    return round(sum(list) / len(list), 1)
