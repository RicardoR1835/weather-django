from multiprocessing import context
from urllib import response
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# the index function is called when root is visited
def index(request):
    API_KEY = os.getenv("API_KEY")

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'

    cities = City.objects.all()

    display = []

    for city in cities:
        print(city)
        print(city.name)
        city_weather = requests.get(url.format(city.name, API_KEY)).json()
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        display.append(weather)

    print(display)
    print("cities are: ", cities)

    # city_weather = requests.get(url.format(city, API_KEY)).json() #request the API data and convert the JSON to Python data types

    # weather = {
    #     'city' : city,
    #     'temperature' : city_weather['main']['temp'],
    #     'description' : city_weather['weather'][0]['description'],
    #     'icon' : city_weather['weather'][0]['icon']
    # }

    context = {
        "weather": display
    }

    # print(city_weather)
    return render(request, "weather/index.html", context)

def add_city(request):
    print("in add_city")
    if request.method == "POST":
        print("in post")
        city = City.objects.create(name=request.POST['city'])
        print(city.name)
        return redirect('/')
