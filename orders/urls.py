from django.urls import path
from . import views


urlpatterns = [
   
    path('place_order/<int:car_id>/', views.place_order, name='place_order'),
   
]