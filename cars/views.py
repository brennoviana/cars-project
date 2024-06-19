from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Car
from .forms import CarForm
from django.contrib.auth.mixins import LoginRequiredMixin

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
        return super().form_valid(form)

class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('cars')

class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'cars/car_confirm_delete.html'
    success_url = reverse_lazy('cars')
