from django.urls import path
from .views import CartView, ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CartView.as_view(), name='checkout'),
    path('order/', CartView.as_view(), name='order'),
    path('compare/', CartView.as_view(), name='compare'),
    path('wishlist/', CartView.as_view(), name='wishlist'),
]
