from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.dashboard, name='dashboard'),
    path('orders/', views.orders, name='admin_orders'),
]