from django.shortcuts import render
from car.models import Car
from orders.models import Orders

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):
    if request.user.is_admin:
        cars = Car.objects.all().order_by('-created_date')
        return render(request, 'admin_dashboard/dashboard.html', {'cars': cars})
    else:
        return render(request, 'admin_dashboard/access_denied.html')
    
    
@login_required(login_url='login')
def orders(request):
    if request.user.is_admin:
        orders = Orders.objects.all().order_by('-created_at')
        return render(request, 'admin_dashboard/orders.html', {'orders': orders})
    else:
        return render(request, 'admin_dashboard/access_denied.html')
