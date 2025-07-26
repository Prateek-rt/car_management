from django.shortcuts import render, redirect
from .forms import CarForm
from .models import Car
from .forms import CustomerForm
from .models import Customer
from django.shortcuts import render, get_object_or_404
from .models import Customer
from django.db.models import Q


def index(request):
    return render(request, "car_dealership/index.html")

def car_list(request):
    cars = Car.objects.all().order_by('-id')  # newest first
    return render(request, 'car_dealership/cars.html', {'cars': cars})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_list')  # after saving redirect to cars list
    else:
        form = CarForm()
    return render(request, 'car_dealership/add_car.html', {'form': form})

def add_customer(request):
    return render(request, "car_dealership/add_customer.html")

def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, "car_dealership/add_customer.html", {"form": form})

def customer_list(request):
    customers = Customer.objects.all().order_by('-id')
    return render(request, "car_dealership/customer_list.html", {"customers": customers})

def customer_list(request):
    customers = Customer.objects.all()

    name = request.GET.get('name')
    gender = request.GET.get('gender')
    car = request.GET.get('car')
    repair_status = request.GET.get('repair_status')

    if name:
        customers = customers.filter(name__icontains=name)
    if gender:
        customers = customers.filter(gender=gender)
    if car:
        customers = customers.filter(car__icontains=car)
    if repair_status:
        customers = customers.filter(repair_status=repair_status)

    return render(request, 'car_dealership/customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'car_dealership/customer_detail.html', {'customer': customer})

def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'car_dealership/add_customer.html', {'form': form, 'editing': True})