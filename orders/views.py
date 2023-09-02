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

            return redirect('user_orders')
        except Exception as e:
            print(str(e))
            pass

    return redirect('car_detail')

@login_required(login_url='login')
def user_orders(request):
    
     current_user = request.user
     orders = Orders.objects.filter(user=current_user)
     orders_count = orders.count()
     

     context = {
        'orders': orders,
        'orders_count': orders_count,
      }
     return render(request, 'orders/user_orders.html', context)
 
 
 
@login_required(login_url='login')
def mark_order_complete(request, order_id):
    if request.user.is_admin:
        try:
            order = Orders.objects.get(id=order_id)
            if order.status == 'Pending':
                order.status = 'Completed'
                order.save()
                return redirect('admin_orders')
        
        except Orders.DoesNotExist:
            pass
    else:
        return render(request, 'admin_dashboard/access_denied.html')
