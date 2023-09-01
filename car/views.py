from django.shortcuts import render
from car.models import Car

# Create your views here.

def car_detail(request, brand_slug, car_slug):
    try:
        single_car = Car.objects.get(brand__slug=brand_slug, slug=car_slug)
        features_list = single_car.features.split(",")
    except Exception as e:
        raise e
    

    context = {
        'single_car': single_car,
        'features_list': features_list
    }
    return render(request, 'car/car_detail.html', context)
