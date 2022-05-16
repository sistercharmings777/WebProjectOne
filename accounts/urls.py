from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),
     
    path('create_order/<str:pk>/', views.createOrder, name="createorder"),
    path('update_order/<str:pk>/', views.updateOrder, name="updateorder"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="deleteorder"),
]
