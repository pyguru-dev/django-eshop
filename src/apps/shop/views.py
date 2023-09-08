from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
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

class WishListView(TemplateView):
    template_name = "shop/wishlist.html"


class CheckoutView(LoginRequiredMixin,TemplateView):
    template_name = "shop/checkout.html"
