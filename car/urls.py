from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('brand/<slug:brand_slug>/<slug:car_slug>/', views.car_detail, name='car_detail'),
    path('create_car/', views.create_car, name='create_car'),
    path('update_car/<int:car_id>/', views.update_car, name='update_car'),
]