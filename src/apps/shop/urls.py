from django.urls import path
from .views import (
    CartView, CheckoutView, ProductListView, ProductDetailView, CompareView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:product_id>', ProductDetailView.as_view(), name='product_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order/', CartView.as_view(), name='order'),
    path('compare/', CompareView.as_view(), name='compare'),
    path('wishlist/', CartView.as_view(), name='wishlist'),
]
