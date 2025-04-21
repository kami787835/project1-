from rest_framework import generics
from .models import Car, economy, Business, Crossover, SUV, Minivan
from .serializers import CarSerializer, economySerializer, BusinessSerializer, CrossoverSerializer, SUVSerializer, \
    MinivanSerializer


class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class economyListCreateAPIView(generics.ListCreateAPIView):
    queryset = economy.objects.all()
    serializer_class = economySerializer

class BusinessListCreateView(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class CrossoverListCreateView(generics.ListCreateAPIView):
    queryset = Crossover.objects.all()
    serializer_class = CrossoverSerializer

class SUVListCreateView(generics.ListCreateAPIView):
    queryset = SUV.objects.all()
    serializer_class = SUVSerializer

class MinivanListCreateView(generics.ListCreateAPIView):
    queryset = Minivan.objects.all()
    serializer_class = MinivanSerializer