from django.urls import path
from .views import CityWeatherView

urlpatterns = [
    path('weather/', CityWeatherView.as_view(), name='city-weather'),
]
