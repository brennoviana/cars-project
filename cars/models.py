from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=50)  
    model = models.CharField(max_length=50) 
    year = models.PositiveIntegerField()  
    color = models.CharField(max_length=30)  
    vin = models.CharField(max_length=17, unique=True) 

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
