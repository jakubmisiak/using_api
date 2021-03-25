import requests
from django.shortcuts import render, redirect

from api.forms import CityForm
from api.models.city import City


def home(request):
    #API from https://openweathermap.org/current
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={Your api key}'

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    weather_data=[]
    cities = City.objects.all()
    form = CityForm()

    for x in cities:
        r = requests.get(url.format(x.name)).json()

        city_weather = {
            'city': x.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        print(city_weather)
        weather_data.append(city_weather)

    context = {
        'weather_data':weather_data,
        'form':form
    }
    return render(request, 'home.html', context)


def city(request, id):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=d3a35b1d63ecb69353b581db27e0f8fb'
    obj = City.objects.get(id=id)
    r = requests.get(url.format(obj.name)).json()

    city_weather = {
        'city': obj.name,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    context = {
        'city_weather': city_weather
    }

    return render(request, 'city.html', context)