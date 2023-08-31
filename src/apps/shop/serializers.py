from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # category = CategorySerializer(many=False)
    # tags = TagSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'published_status', 'url']
