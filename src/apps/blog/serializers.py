from rest_framework import serializers
from .models import Category, Tag, Post, Comment


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'url']


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'url']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=False)
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['title', 'category', 'url']
