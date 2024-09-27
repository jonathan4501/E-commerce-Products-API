from django.urls import path, include
from rest_framework import routers
from .views import ProductListView, ProductDetailView, CreateProductView, UpdateProductView, DeleteProductView, UserListView, UserDetailView, CreateUserView, UpdateUserView, DeleteUserView, LoginView

router = routers.DefaultRouter()
router.register(r'products', ProductListView, basename='products')
router.register(r'users', UserListView, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('products/<pk>/', ProductDetailView.as_view()),
    path('create-product/', CreateProductView.as_view()),
    path('update-product/<pk>/', UpdateProductView.as_view()),
    path('delete-product/<pk>/', DeleteProductView.as_view()),
    path('users/<pk>/', UserDetailView.as_view()),
    path('create-user/', CreateUserView.as_view()),
    path('update-user/<pk>/', UpdateUserView.as_view()),
    path('delete-user/<pk>/', DeleteUserView.as_view()),
    path('login/', LoginView.as_view()),
]