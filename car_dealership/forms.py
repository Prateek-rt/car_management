from django import forms
from .models import Car
from .models import Customer

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'model', 'price', 'mileage', 'image']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }