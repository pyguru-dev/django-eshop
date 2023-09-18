import graphene
from graphene import Mutation
from graphene_django.forms.mutation import DjangoFormMutation
from apps.shop.models import ProductCategory

from apps.shop.schema import ProductCategoryNode

class ProductCategoryMutation(Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String(required=True)
    
    category = graphene.Field(ProductCategoryNode)
    
    @classmethod
    def mutate(root, info, id, title):
        category = ProductCategory.objects.get(pk=id)
        category.title = title
        category.save()
        
        return ProductCategoryMutation(category=category)