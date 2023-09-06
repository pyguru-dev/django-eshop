import graphene
from graphene_django import DjangoObjectType

from apps.blog.models import BlogCategory

class BlogCategoryType(DjangoObjectType):
    class Meta:
        model = BlogCategory
        fields = ("id", "name")

class Query(graphene.ObjectType):
    all_categories = graphene.List(BlogCategoryType)
    # category_by_name = graphene.Field(BlogCategoryType, name=graphene.String(required=True))

    def resolve_all_categories(root, info):        
        return BlogCategory.objects.all()

    def resolve_category_by_name(root, info, name):
        try:
            return BlogCategory.objects.get(name=name)
        except BlogCategory.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)