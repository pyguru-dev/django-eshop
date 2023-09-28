from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Brand, Order, OrderItem, Product, ProductCategory, Wishlist


class ProductListView(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'shop/product_list.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.all()
        return context


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_products"] = Product.objects.all()
        # context["related_products"] = Product.objects.filter(category=product.category).exclude(pk=product.id)
        context["popular_products"] = Product.objects.all()
        return context

    # def get_queryset(self):
    #     order_id = self.kwargs['pk']
    #     order = Order.objects.get(id=order_id)
    #     order_items = OrderItem.objects.filter(order=order)
    #     return order_items


# class ProductDocumentViewSet(DocumentViewSet):
#     document = ProductDocument
#     serializer_class = ProductDocumentSerializer

#     filter_backends = (
#         FilteringFilterBackend,
#         SearchFilterBackend,
#         SuggesterFilterBackend,
#     )

#     search_fields = ("name",)

#     filter_fields = {
#         "id": {"field": "id", "lookups": [LOOKUP_QUERY_IN]},
#         "price": {"field": "price", "lookups": [LOOKUP_QUERY_GTE, LOOKUP_FILTER_RANGE]},
#     }

#     suggester_fields = {
#         "name_suggest": {"field": "name.suggest", "suggesters": [SUGGESTER_COMPLETION]}
#     }


class CartView(TemplateView):
    template_name = "shop/cart.html"


class BrandListView(ListView):
    model = Brand
    template_name = "shop/brand_list.html"
    context_object_name = 'brands'


class BrandDetailView(DetailView):
    model = Brand
    template_name = "shop/brand_detail.html"
    context_object_name = 'brand'


class CategoryListView(ListView):
    model = ProductCategory
    template_name = "shop/category_list.html"
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = ProductCategory
    template_name = "shop/category_detail.html"
    context_object_name = 'category'


class CompareView(TemplateView):
    template_name = "shop/compare.html"


class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = "shop/checkout.html"


class WishListView(ListView):
    template_name = "shop/wishlist.html"
    model = Wishlist
    context_object_name = 'wishlist'


@login_required(login_url='login_view')
def wishlist_add(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user)
        messages.success(request, 'remove')
    else:
        product.users_wishlist.add(request.user)
        messages.success(request, 'added')


@login_required(login_url='login_view')
def wishlist_remove(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
