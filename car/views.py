from django.shortcuts import render, redirect, get_object_or_404
from car.models import Car
from django.contrib.auth.decorators import login_required
from .forms import CarForm
from django.contrib import messages

# Create your views here.

def cars(request):
     cars = Car.objects.filter(is_available=True)

     context = {
        'cars': cars,
      }
     return render(request, 'car/cars.html', context)


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


@login_required(login_url='login')
def create_car(request):
    if request.user.is_admin:
        if request.method == 'POST':
            print(request.POST)
            form = CarForm(request.POST, request.FILES)
            
            if form.is_valid():
                print('data', form.cleaned_data)
                form.save()
                
                return redirect('dashboard')  
        else:
            form = CarForm()
           
        return render(request, 'admin_dashboard/add_car.html', {'form': form})
       
    else:
        return render(request, 'admin_dashboard/access_denied.html')
    

@login_required(login_url='login')
def update_car(request, car_id):
    if request.user.is_admin:
    
        car = get_object_or_404(Car, id=car_id)

        if request.method == 'POST':
            form = CarForm(request.POST, request.FILES, instance=car)
            if form.is_valid():
                form.save()
               
        else:
            form = CarForm(instance=car)

        return render(request, 'admin_dashboard/update_car.html', {'form': form, 'car_id': car_id})
    
    else:
        return render(request, 'admin_dashboard/access_denied.html')
    
   
    
