from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path('cars/', views.car_list, name='car_list'),
    path('add_car/', views.add_car, name='add_car'),
    path('add_customer/', views.add_customer, name='add_customer'), 
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('edit_customer/<int:customer_id>/', views.edit_customer, name='edit_customer'),
    path('workers/', views.worker_view, name='worker_list'),
    path('add-worker/', views.add_worker_ajax, name='add_worker_ajax'),
    path('cars_detail/<int:pk>/', views.car_detail, name='car_detail'),


]