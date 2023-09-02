from django.urls import path
from . import views
from car.views import create_car

urlpatterns = [
    path('cars/', views.dashboard, name='dashboard'),
    path('orders/', views.orders, name='admin_orders'),
    path('create_car/', create_car, name='create_car'),
]