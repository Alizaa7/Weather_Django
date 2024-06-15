from django.shortcuts import render
from .utils import get_weather_data, get_forecast_data
from django.conf import settings
from datetime import datetime

def home(requests):
    if 'city' in requests.GET:
        city = requests.GET['city']
        api_key = settings.OPENWEATHERMAP_API_KEY
        weather_data = get_weather_data(city, api_key)
        forecast_data = get_forecast_data(city, api_key)
    else:
        weather_data = forecast_data = None    


    context= {
        'weather': weather_data,
        'forecast': forecast_data
    }
    return render(requests, 'weather/home.html', context)