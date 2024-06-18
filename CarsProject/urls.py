from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('cars/', include('cars.urls')),
]

from CarsProject.errors import custom_page_not_found_view

handler404 = custom_page_not_found_view
