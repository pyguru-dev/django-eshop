from graphene import relay, ObjectType, Mutation
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoFormMutation
from .models import Post, BlogCategory, Comment


class BlogCategoryNode(DjangoObjectType):
    class Meta:
        model = BlogCategory
        filter_fields = ("id", 'slug', "name")
        interfaces = (relay.Node,)


class PostNode(DjangoObjectType):
    class Meta:
        model = Post
        filter_fields = ('id', 'uuid', 'title', 'slug', 'author', 'created_at')
        # exclude = ()
        interfaces = (relay.Node,)

# class PostMutation(DjangoFormMutation):
#     class Meta:
#         form_class = PostCreationForm


class Query(ObjectType):
    all_posts = DjangoFilterConnectionField(PostNode)

    all_blog_categories = DjangoFilterConnectionField(BlogCategoryNode)
