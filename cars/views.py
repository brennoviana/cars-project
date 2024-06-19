from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Car
from .forms import CarForm

class CarListView(ListView):
    model = Car
    template_name = 'cars/cars.html'
    context_object_name = 'cars'

class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('cars')

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('cars')

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'cars/car_confirm_delete.html'
    success_url = reverse_lazy('cars')
