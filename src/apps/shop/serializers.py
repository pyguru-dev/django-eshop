from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import (Product, ProductCategory,
                     Order, Banner, Brand, Cart, Discount,
                     Giftcode, Shipping, Warranty)


class ProductSerializer(HyperlinkedModelSerializer):
    # category = CategorySerializer(many=False)
    # tags = TagSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'published_status', 'url']


class ProductCategorySerializer(ModelSerializer):
    pass

class BrandSerializer(ModelSerializer):
    pass

class CartSerializer(ModelSerializer):
    pass

class ShippingSerializer(ModelSerializer):
    pass

class WarrantySerializer(ModelSerializer):
    pass

class DiscountSerializer(ModelSerializer):
    pass

class OrderSerializer(ModelSerializer):
    pass

class OrderDetailSerializer(ModelSerializer):
    pass
