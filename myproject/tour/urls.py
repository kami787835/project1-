from django.urls import path
from .views import *

urlpatterns = [
    path('tours/', TourListAPIView.as_view()),
    ]