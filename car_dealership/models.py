from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    mileage = models.CharField(max_length=20)
    image = models.ImageField(upload_to='car_images/')

class Customer(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    car = models.CharField(max_length=100)
    date = models.DateField()
    photo = models.ImageField(upload_to='customer_photos/', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    problem_description = models.TextField()
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    repair_status = models.CharField(max_length=20, default='Pending')

class Worker(models.Model):
    worker_id=models.CharField(max_length=100,default="WRK-001", unique=True)
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    email_id = models.EmailField()
    address = models.TextField(blank=True)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name
