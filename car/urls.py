from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('brand/<slug:brand_slug>/<slug:car_slug>/', views.car_detail, name='car_detail'),
]