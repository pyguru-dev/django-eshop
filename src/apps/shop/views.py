from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

class ProductListView(ListView):
    pass

class ProductDetailView(DetailView):
    pass

class CartView(TemplateView):
    pass

