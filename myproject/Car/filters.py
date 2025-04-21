import django_filters
from .models import Car

class CarFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = {
            'manufacturer': ['exact'],
            'model': ['exact'],
            'mileage': ['exact', 'gte', 'lte'],
            # Добавьте другие поля модели Car, которые вы хотите использовать для фильтрации
        }