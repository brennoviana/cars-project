from django.urls import path
from .views import carsView

urlpatterns = [
    path('/', carsView.as_view(), name='cars'),
]
