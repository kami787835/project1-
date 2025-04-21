from django.db import models

class Tour(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    duration_days = models.IntegerField(null=True, blank=True)
    destination = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    car_image = models.ImageField(upload_to='tour_images/', null=True, blank=True)

    def __str__(self):
        return self.title if self.title else 'Unnamed Tour'