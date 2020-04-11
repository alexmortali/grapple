from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginator_function(request, paginator):
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
    return round(sum(list) / len(list), 1)
