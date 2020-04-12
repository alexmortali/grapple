from django.conf.urls import url
from . import views
app_name = 'products'

urlpatterns = [
    url(r'^$', views.list_of_products, name='list_of_products'),
    url(r'^(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^category/(?P<category_slug>[-\w]+)/$',
        views.list_of_products_by_category,
        name='list_of_products_by_category'
        )
]
