from rest_framework.throttling import UserRateThrottle
import datetime
import requests
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics, mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotAcceptable
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from apps.api.renderers import UserRenderer
from apps.api.serializers import RequestOtpResponseSerializer, RequestOtpSerializer, UserChangePasswordSerializer, UserForgotPasswordSerializer, UserLoginSerializer, UserRegisterSerializer, VerifyOtpSerializer
from apps.shop.models import Cart, Product
from apps.shop.serializers import ProductSerializer
from apps.blog.models import BlogCategory, Post
from apps.payments.models import Gateway, Payment
from apps.payments.serializers import PaymentSerializer, GatewaySerializer
from apps.blog.serializers import (CategoryTreeSerializer, CreateCategoryNodeSerializer,
                                   PostSerializer, CategorySerializer, TagSerializer)
from apps.accounts.models import OtpRequest, User
from apps.core.models import Tag
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


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


class CategoryListView(APIView):
    def get_queryset(self):
        return Category.objects.all()

    def get(self, request):

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class BlogCategoryViewSet(ModelViewSet):

    def get_queryset(self):
        if self.action == 'list':
            return BlogCategory.objects.filter(depth=1)
        else:
            return BlogCategory.objects.all()

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


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PostViewSet(ModelViewSet):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# class RegisterView(APIView):
#     def post(self, request):
#         mobile = request.data.get('mobile')
#         if not mobile:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#         user, created = User.objects.get_or_create(mobile=mobile)
#         if not created:
#             return Response({'data': 'user registered'}, status=status.HTTP_400_BAD_REQUEST)

#         code = random.randint(10000, 99999)

#         # send sms

#         return Response({'code': code})


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            context = {
                'token': token,
                'user': user,
                'message': 'registration is successful'
            }
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                context = {'user': user, 'token': token,
                           'msg': 'login successful'}
                return Response(context, status=status.HTTP_200_OK)
            else:
                return Response('email or password is wrong', status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.get(email=email)
        if user is None:
            raise AuthenticationFailed('user not found')

        if not user.check_password(password):
            raise AuthenticationFailed('password wrong')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=50),
            'iat': datetime.datetime.utcnow()
        }

        # PyJwt
        token = jwt.encode(payload, 'secret',
                           algorithm='HS256').decode('utf-8')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self,  request, format=None):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('unauthenticate')

        try:
            payload = jwt.decode(token, 'secret', algorithm='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('un authenticate')

        user = User.objects.get(id=payload['id'])
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)


class UserLogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {'message': 'logout'}
        return Response(response)


class UserForgotPasswordAPIView(APIView):
    def post(self, request):
        serializer = UserForgotPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'password reset link sent'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPasswordResetAPIView(APIView):
    def post(self, request, uid, token):
        serializer = UserPasswordSerializer(data=request.data)
        context = {'uid': uid, 'token': token}
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'password reset successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserChangePasswordAPIView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data)
        context = {'user': request.user, 'msg': 'password changed'}
        if serializer.is_valid(raise_exception=True):
            return Response(context, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["POST"])
# def register(request):
#     if request.method == 'POST':
#         serializer = RegisterSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             user = serializer.save()
#             data['token'] = Token.objects.get(user=user).key
#             data['message'] = 'register is ok'
#             return Response(data)


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


# class UserProfileView(APIView):

#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         pass

#     def put(self, request, pk):
#         user_profile = UserProfile.objects.get(pk=pk)
#         serializer = UserProfileSerializer(
#             instance=user_profile,
#             data=request.data
#         )

#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response('profile updated')

def search(request):
    if request.method == 'POST':
        query = request.POST.get('q')
        if query:
            query_for_search = SearchQuery(query)
            search_vector = SearchVector(
                'title', weight='A') + SearchVector('body', weight='B')
            search_rank = SearchRank(search_vector, query_for_search)
            posts = Post.objects.published.annotate(search=search_vector, rank=search_rank) \
                .filter(search=query_for_search).order_by('-rank')
            return Response({'posts': posts})


def add_to_cart(request):
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            product_id = request.POST.get('product_id')
            product = Product.objects.get(id=product_id)
            if product:
                if Cart.objects.filter(user=user, product_id=product_id):
                    return 'product is already in card'
                else:
                    quantity = 1
                    Cart.objects.create(
                        user=user, product_id=product_id, quantity=quantity)
                    return 'added'
            else:
                return 'product not found'
        else:
            pass


def update_cart_quantity(request):
    product_id = request.POST.get('product_id')
    action = request.POST.get('action')

    cart_item = Cart.objects.filter(
        user=request.user, product_id=product_id)[0]
    if cart_item:
        if action == 'add':
            cart_item.quantity += 1
        elif action == 'decrease':
            cart_item -= 1

        cart_item.save()

    return 'update'


def checkout(request):
    context = {}
    user = request.user
    cart_items = Cart.objects.filter(user=user)

    context['cart_items'] = cart_items
    context['cart_items_count'] = cart_items.count()

    total_price = 0
    if cart_items:
        for item in cart_items:
            total_price += item.product.price

        context['total_price'] = total_price


############ OTP ############


class OncePerMinuteThrottle(UserRateThrottle):
    rate = '1/minute'


class RequestOtpAPIView(APIView):

    # throttle_classes = [OncePerMinuteThrottle]

    def post(self, request):
        serializer = RequestOtpSerializer(data=request.data)
        if serializer.is_valid():
            mobile = serializer.validated_data['mobile']
            channel = serializer.validated_data['channel']
            otp_request = OtpRequest(mobile=mobile, channel=channel)
            otp_request.generate_otp()
            otp_request.save()

            # Send sms

            return Response(RequestOtpResponseSerializer(otp_request).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOtpAPIView(APIView):
    def post(self, request):
        serializer = VerifyOtpSerializer(data=request.data)
        if serializer.is_valid():
            request_id = serializer.validated_data['request_id']
            mobile = serializer.validated_data['mobile']
            password = serializer.validated_data['password']

            otp_request = OtpRequest.objects.filter(
                request_id=request_id,
                mobile=mobile,
                valid_until__gte=timezone.now()
            )
            if otp_request.exists():
                userq = User.objects.filter(mobile=mobile)
                if userq.exists():
                    user = userq.first()
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({'token': token, 'new_user': False})
                else:
                    user = User.objects.create(mobile=mobile)
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({'token': token, 'new_user': True})

            else:
                return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
