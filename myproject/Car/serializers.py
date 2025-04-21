from rest_framework import serializers
from .models import Car, economy, Business, Crossover, SUV, Minivan


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class economySerializer(serializers.ModelSerializer):
    class Meta:
        model = economy
        fields = '__all__'

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class CrossoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crossover
        fields = '__all__'

class SUVSerializer(serializers.ModelSerializer):
    class Meta:
        model = SUV
        fields = '__all__'

class MinivanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minivan
        fields = '__all__'