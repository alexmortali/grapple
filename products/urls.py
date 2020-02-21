from django.conf.urls import url
from .views import All_Products, SingleCategoryView, ProductDetailView
app_name = 'products'

urlpatterns = [
    url('', All_Products.as_view(), name='all_products'),
    url(r'category/<slug>', SingleCategoryView.as_view(), name='category'),
    url(r'product/<slug>', ProductDetailView.as_view(), name='product_detail'),
]