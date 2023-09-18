from graphene import ObjectType, Schema

from apps.blog.schema import Query as BlogQuery
from apps.shop.mutations import ProductCategoryMutation
from apps.shop.schema import Query as ShopQuery
from apps.accounts.schema import Query as AccountQuery
# from apps.vendors.schema import Query as VendorQuery
# from apps.shortener.schema import Query as ShortenerQuery


class Query(BlogQuery, ShopQuery, AccountQuery, ObjectType):
    pass


class Mutation(ObjectType):
    # update_product_category = ProductCategoryMutation.Field()
    pass


# schema = Schema(query=Query, mutation=Mutation)
schema = Schema(query=Query)
