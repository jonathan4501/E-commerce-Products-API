from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Category, CustomUser
from .serializers import ProductSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class ProductListView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'category__name']
    filterset_fields = ['category', 'price', 'stock_quantity']

    def custom_action(self, request):
        products = self.queryset.all()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(products, request)
        serializer = self.serializer_class(page, many=True)
        return paginator.get_paginated_response(serializer.data)

class ProductDetailView(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk):
        product = self.queryset.get(pk=pk)
        serializer = self.serializer_class(product)
        return Response(serializer.data)

class UserListView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        users = self.queryset.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

class UserDetailView(APIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get(self, request, pk):
        user = self.queryset.get(pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

class CreateProductView(APIView):
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateProductView(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def put(self, request, pk):
        product = self.queryset.get(pk=pk)
        serializer = self.serializer_class(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteProductView(APIView):
    queryset = Product.objects.all()

    def delete(self, request, pk):
        product = self.queryset.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CreateUserView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateUserView(APIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def put(self, request, pk):
        user = self.queryset.get(pk=pk)
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteUserView(APIView):
    queryset = CustomUser.objects.all()

    def delete(self, request, pk):
        user = self.queryset.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            })
        return Response({'error': 'Invalid credentials'}, status=401)