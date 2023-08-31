from rest_framework import serializers
from .models import Category, Tag, Post, Comment


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'url']


class CreateCategoryNodeSerializer(serializers.HyperlinkedModelSerializer):

    parent = serializers.IntegerField(required=False)

    def create(self, validated_data):
        parent = validated_data.pop('parent', None)

        if parent is None:
            instance = Category.add_root(**validated_data)
        else:
            parent_node = get_object_or_404(Category, pk=parent)
            instance = parent_node.add_child(**validated_data)
        return instance

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'is_active', 'url', 'parent']


class CategoryTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        return CategoryTreeSerializer(obj.get_children(), many=True).data

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'is_active', 'children']


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'url']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=False)
    # tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['title', 'category', 'url']
