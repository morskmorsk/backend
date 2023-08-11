from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    ordering = ['name']
    paginate_by = 10


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'
    context_object_name = 'products'
    ordering = ['name']
    paginate_by = 10
