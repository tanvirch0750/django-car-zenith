from django.shortcuts import render, redirect, get_object_or_404
from car.models import Car
from .models import Orders
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
import datetime
from django.db import transaction

# Create your views here.
@login_required(login_url='login')
def place_order(request, car_id):
    current_user = request.user
    car = Car.objects.get(id=car_id)

    if current_user.is_authenticated:
        try:
            with transaction.atomic():
                order_item = Orders.objects.create(
                    user=current_user,
                    car=car,
                    status='Pending'
                )

                timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                order_number = f'ORD-{timestamp}-{order_item.id}'
                order_item.order_number = order_number
                order_item.save()

            return redirect('cars')
        except Exception as e:
            print(str(e))
            pass

    return redirect('cars')
