from django.shortcuts import render, redirect
from .forms import CarForm
from .models import Car
from .forms import CustomerForm
from .models import Customer
from django.shortcuts import render, get_object_or_404
from .models import Customer
from django.db.models import Q
from django.http import JsonResponse
from .models import Worker
from .forms import WorkerForm
from django.http import JsonResponse, Http404

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

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'car_dealership/car_details.html', {'car': car})

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

def worker_view(request):
    form = WorkerForm()
    workers = Worker.objects.all().order_by('-id')
    return render(request, 'car_dealership/workers.html', {'form': form, 'workers': workers})

def add_worker_ajax(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            worker = form.save()
            return JsonResponse({
                'status': 'success',
                'worker': {
                    'worker_id':Worker.worker_id,
                    'name': worker.name,
                    'mobile_no': worker.mobile_no,
                    'email_id': worker.email_id,
                    'position': worker.position
                }
            })
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

