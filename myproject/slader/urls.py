from django.urls import path
from .views import *

urlpatterns = [
    path('slider/', SliderListAPIView.as_view()),
    path('items/', ItemListAPIView.as_view()),
    path('about/', AboutUsListCreateView.as_view()),
    path('contacts/', ContactsListCreateView.as_view()),
    path('reviews/', ClientReviewListCreateView.as_view()),
    ]