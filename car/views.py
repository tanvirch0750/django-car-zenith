from django.shortcuts import render, redirect
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
    
   
    
