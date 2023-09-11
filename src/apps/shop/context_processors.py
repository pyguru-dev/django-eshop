from .cart import Cart
from .models import Cart as CartModel, ProductCategory


def cart_count(request):
    context = {}
    cart_total = 0

    if request.user.is_authenticate:
        cart_items = CartModel.objects.filter(user=request.user)
        if cart_items:
            for item in cart_items:
                cart_total += item.quantity
            context['cart_total'] = cart_total
    else:
        context['cart_total'] = 0

    return context


def cart(request):
    return {'cart': Cart(request)}

def menu_categories(request):
    categories = ProductCategory.objects.filter(parent=None)

    return {'menu_categories': categories}