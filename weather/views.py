# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=39126240d99ed0c47c6bc87a50151335'

    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()  # both saves and validates it

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        weather_data.append(city_weather)

    print(weather_data)

    context = {"weather_data": weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)
