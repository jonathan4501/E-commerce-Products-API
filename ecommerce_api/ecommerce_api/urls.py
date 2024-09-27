"""
URL configuration for ecommerce_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from products import views  

router = routers.DefaultRouter()
router.register(r'products', views.ProductListView, basename='products')
router.register(r'users', views.UserListView, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('api/products/<pk>/', views.ProductDetailView.as_view()),
    path('api/create-product/', views.CreateProductView.as_view()),
    path('api/update-product/<pk>/', views.UpdateProductView.as_view()),
    path('api/delete-product/<pk>/', views.DeleteProductView.as_view()),
    path('api/users/<pk>/', views.UserDetailView.as_view()),
    path('api/create-user/', views.CreateUserView.as_view()),
    path('api/update-user/<pk>/', views.UpdateUserView.as_view()),
    path('api/delete-user/<pk>/', views.DeleteUserView.as_view()),
    path('api/login/', views.LoginView.as_view()),
]