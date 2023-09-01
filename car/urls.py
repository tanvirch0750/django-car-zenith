from django.urls import path
from . import views
urlpatterns = [
    path('brand/<slug:brand_slug>/<slug:car_slug>/', views.car_detail, name='car_detail'),
]