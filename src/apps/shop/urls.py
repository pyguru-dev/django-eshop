from django.urls import path
from .views import (
    CartView, CheckoutView, ProductListView,
    ProductDetailView, CompareView, WishListView,
    BrandListView, BrandDetailView, wishlist_add, wishlist_remove,
)


# app_name = 'apps.shop'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<str:slug>/detail/', ProductDetailView.as_view(), name='product_detail'),
    # re_path(r'detail/(?P<article_slug>[-\w]+)/', article_detail, name='article_detail')
    
    path('categories/', BrandListView.as_view(), name='product_category_list'),
    path('categories/<str:slug>/', BrandDetailView.as_view(), name='product_category_detail'),
    path('brands/', BrandListView.as_view(), name='brand_list'),
    path('brands/<str:slug>/', BrandDetailView.as_view(), name='brand_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order/', CartView.as_view(), name='order'),
    path('order/<uuid:uuid>/invoice', CartView.as_view(), name='order_invoice'),
    path('compare/', CompareView.as_view(), name='compare'),
    path('wishlist/', WishListView.as_view(), name='wishlist'),
    path('wishlist/<int:product_id>/add', wishlist_add, name='wishlist_add'),
    path('wishlist/<int:product_id>/remove', wishlist_remove, name='wishlist_remove'),
]
