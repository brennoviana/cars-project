from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Car
from .forms import CarForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class CarListView(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'cars/cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.filter(creator=self.request.user)

class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('cars')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request, 'Car successfully created!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error creating the car.')
        return super().form_invalid(form)

class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('cars')

    def form_valid(self, form):
        messages.success(self.request, 'Car successfully updated!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error updating the car.')
        return super().form_invalid(form)

class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'cars/car_confirm_delete.html'
    success_url = reverse_lazy('cars')

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, 'Car successfully deleted!')
        return super().delete(request, *args, **kwargs)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error deleting the car.')
        return super().form_invalid(form)