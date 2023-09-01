from django.urls import path
from . import views


urlpatterns = [
   
    path('place_order/<int:car_id>/', views.place_order, name='place_order'),
    path('user_orders/', views.user_orders, name='user_orders'),
   
]