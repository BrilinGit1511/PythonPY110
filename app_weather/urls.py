from django.urls import path
from .views import my_view, weather_view

urlpatterns = [
    path('weather/', my_view),
    path('weather_view/', weather_view)
]