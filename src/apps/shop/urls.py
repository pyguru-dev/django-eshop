from django.urls import path
from .views import (
    CartView, CheckoutView, ProductListView,
    ProductDetailView, CompareView, WishListView,
    BrandListView, BrandDetailView,
)


# app_name = 'apps.shop'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<slug:slug>/detail/', ProductDetailView.as_view(), name='product_detail'),
    # re_path(r'detail/(?P<article_slug>[-\w]+)/', article_detail, name='article_detail')

    path('brands/', BrandListView.as_view(), name='brand_list'),
    path('brands/<slug:slug>/', BrandDetailView.as_view(), name='brand_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order/', CartView.as_view(), name='order'),
    path('compare/', CompareView.as_view(), name='compare'),
    path('wishlist/', WishListView.as_view(), name='wishlist'),
]
