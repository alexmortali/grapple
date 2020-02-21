from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from .forms import QuantityForm, SizeForm
from .models import Category, Product
# Create your views here.

class All_Products(ListView):
    """ List view for all products """

    template_name = "products/categories.html"
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = 'All Products'
        return context

    def get_queryset(self):
        return self.queryset

class SingleCategoryView(SingleObjectMixin, All_Products):
    """ View inheriting from All_products to show products within a 
        single category """

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Category.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.object
        return context

    def get_queryset(self):
        return self.object.product_set

class ProductDetailView(DetailView):
    """ Single Product view, uses detail view to show a single product """

    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form1'] = QuantityForm()
        context['form2'] = SizeForm()
        return context
