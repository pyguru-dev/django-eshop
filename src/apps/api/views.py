from django.shortcuts import get_object_or_404
from rest_framework import status, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.shop.models import Product
from apps.shop.serializers import ProductSerializer
from apps.blog.models import Category, Post, Tag
from apps.blog.serializers import PostSerializer, CategorySerializer, TagSerializer


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class TagListView(APIView):
    def get(self, request):
        categories = Tag.objects.all()
        serializer = TagSerializer(categories, many=True)
        return Response(serializer.data)
