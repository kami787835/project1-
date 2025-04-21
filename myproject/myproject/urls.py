"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .yasg import urlpatterns as yasg_urls
from tour.views import TourListAPIView
from slader.views import SliderListAPIView,ItemListAPIView,AboutUsListCreateView,ContactsListCreateView,ClientReviewListCreateView
from Car.views import CarListCreateView,CarDetailView,economyListCreateAPIView,BusinessListCreateView,CrossoverListCreateView,SUVListCreateView,MinivanListCreateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sliders/', SliderListAPIView.as_view(), name='slider-list-create'),
    path('items/', ItemListAPIView.as_view(), name='item-list'),
    path('tours/', TourListAPIView.as_view(), name='tour-list'),
    path('about/', AboutUsListCreateView.as_view(), name='about-list'),
    path('contacts/', ContactsListCreateView.as_view(), name='contacts-list'),
    path('reviews/', ClientReviewListCreateView.as_view(), name='client-reviews-list'),
    path('cars/', CarListCreateView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('economy/', economyListCreateAPIView.as_view(), name='task-list-create'),
    path('business/', BusinessListCreateView.as_view(), name='business-list'),
    path('crossovers/', CrossoverListCreateView.as_view(), name='crossover-list'),
    path('suv/', SUVListCreateView.as_view(), name='suv-list-create'),
    path('minivan/', MinivanListCreateView.as_view(), name='minivan-list-create'),

]
urlpatterns += yasg_urls