import requests
from django.shortcuts import get_object_or_404
from rest_framework import status, generics, mixins, viewsets
from rest_framework.exceptions import NotAcceptable
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from apps.shop.models import Product
from apps.shop.serializers import ProductSerializer
from apps.blog.models import Category, Post, Tag
from apps.payments.models import Gateway, Payment
from apps.payments.serializers import PaymentSerializer, GatewaySerializer
from apps.blog.serializers import CategoryTreeSerializer, CreateCategoryNodeSerializer, PostSerializer, CategorySerializer, TagSerializer
from apps.accounts.serializers import RegisterSerializer

User = get_user_model()


class ProductListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        # products = Product.objects.all().select_related('category')
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


class CategoryViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        if self.action == 'list':
            return Category.objects.filter(depth=1)
        else:
            return Category.objects.all()

    def get_serializer_class(self):
        
        match self.action:
            case 'list':
                return CategoryTreeSerializer
            case 'create':
                return CreateCategoryNodeSerializer
            case 'retrieve':
                return 
            case _:
                raise NotAcceptable()



class TagListView(APIView):
    def get(self, request):
        categories = Tag.objects.all()
        serializer = TagSerializer(categories, many=True)
        return Response(serializer.data)


class RegisterView(APIView):
    def post(self, request):
        mobile = request.data.get('mobile')
        if not mobile:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user, created = User.objects.get_or_create(mobile=mobile)
        if not created:
            return Response({'data': 'user registered'}, status=status.HTTP_400_BAD_REQUEST)

        code = random.randint(10000, 99999)

        # send sms

        return Response({'code': code})


# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer

class GetTokenView(APIView):
    def post(self, request):
        mobile = request.data.get('mobile')
        code = request.data.get('code')


class GatewayListView(APIView):
    def get(self, request):
        categories = Gateway.objects.all()
        serializer = GatewaySerializer(categories, many=True)
        return Response(serializer.data)


class PaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        gateway_id = request.query_params.get("gateway")

        try:
            gateway = Gateway.objects.get(pk=gateway_id)
        except (Gateway.DoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        payment = Payment.objects.create(
            user=request.user,
            gateway=gateway,
            price=0,
            token=str(uuid.uuid4())
        )

        return Response({'token': payment.token, 'callback_url': ''})

    def post(self, request):
        token = request.data.get('token')
        status = request.data.get('status')

        try:
            payment = Payment.objects.get(token=token)
        except Payment.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if status != 10:
            payment.status = Payment.STATUS_CANCELED
            payment.save()
            return Response({'data': "payment failed"})

        req = requests.post('bank_verification_url', data={})

        if req.status_code == 100:
            payment.status = Payment.STATUS_ERROR
            payment.save()
            return Response({'data': "payment failed"})

        payment.status = Payment.STATUS_PAID
        payment.save()

        # save order
        return Response()
