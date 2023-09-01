from django.shortcuts import render
from car.models import Car


def home(request):
    featured_cars = Car.objects.filter(is_featured=True)
    return render(request, 'home.html', {'cars': featured_cars})