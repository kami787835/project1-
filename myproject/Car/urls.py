from django.urls import path
from .views import *
urlpatterns = [
path('cars/', CarListCreateView.as_view()),
path('economy/', economyListCreateAPIView.as_view()),
path('business/', BusinessListCreateView.as_view()),
path('crossovers/', CrossoverListCreateView.as_view()),
path('suv/', SUVListCreateView.as_view()),
path('minivan/', MinivanListCreateView.as_view()),
     ]