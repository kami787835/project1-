from django.db import models

class Car(models.Model):
    manufacturer = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    mileage = models.IntegerField(null=True, blank=True)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    rented_by = models.CharField(max_length=100, null=True, blank=True)
    rental_start_date = models.DateField(null=True, blank=True)
    rental_end_date = models.DateField(null=True, blank=True)
    car_image = models.ImageField(upload_to='car_images/', null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.manufacturer} {self.model} - {self.year}"

class economy(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)

class Business(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Crossover(models.Model):
    field1 = models.CharField(max_length=100, null=True, blank=True)
    field2 = models.TextField(null=True, blank=True)

class SUV(models.Model):
    brand = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

class Minivan(models.Model):
    brand = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)