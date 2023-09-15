from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Brand, ProductCategory, Product, Shipping, Warranty


class WarrantyNode(DjangoObjectType):
    class Meta:
        model = Warranty
        filter_fields = ("id", 'slug', "title")
        interfaces = (relay.Node,)


class ShippingNode(DjangoObjectType):
    class Meta:
        model = Shipping
        filter_fields = ("id", 'amount', "title", 'description')
        interfaces = (relay.Node,)


class BrandNode(DjangoObjectType):
    class Meta:
        model = Brand
        filter_fields = ("id", 'slug', "title")
        interfaces = (relay.Node,)


class ProductCategoryNode(DjangoObjectType):
    class Meta:
        model = ProductCategory
        filter_fields = ("id", 'slug', "name")
        interfaces = (relay.Node,)


class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = ('id', 'uuid', 'title', 'slug', 'author', 'created_at')
        # exclude = ()
        interfaces = (relay.Node,)


class Query(ObjectType):
    all_products = DjangoFilterConnectionField(ProductNode)
    all_brands = DjangoFilterConnectionField(BrandNode)
    all_warranties = DjangoFilterConnectionField(WarrantyNode)
    all_shippings = DjangoFilterConnectionField(ShippingNode)
    all_product_categories = DjangoFilterConnectionField(ProductCategoryNode)
