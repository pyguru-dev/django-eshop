from django.urls import path
from .views import (
    CartView, CheckoutView, ProductListView, ProductDetailView, CompareView,WishListView
)


# app_name = 'apps.shop'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order/', CartView.as_view(), name='order'),
    path('compare/', CompareView.as_view(), name='compare'),
    path('wishlist/', WishListView.as_view(), name='wishlist'),
]
