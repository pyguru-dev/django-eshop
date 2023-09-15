import graphene

from apps.blog.schema import Query as BlogQuery
from apps.shop.schema import Query as ShopQuery


class Query(BlogQuery, ShopQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
