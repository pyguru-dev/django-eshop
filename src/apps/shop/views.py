from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'shop/product_list.html'


class ProductDetailView(DetailView):
    context_object_name = 'product'
    template_name = 'shop/product_detail.html'


class CartView(TemplateView):
    template_name = "shop/cart.html"

class CompareView(TemplateView):
    template_name = "shop/compare.html"


class CheckoutView(TemplateView):
    template_name = "shop/checkout.html"
