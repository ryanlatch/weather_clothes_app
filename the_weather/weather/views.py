from django.shortcuts import render, redirect
from . import keys
from .models import City
from .forms import CityForm
import requests



# Create your views here.
def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'

    # get all the cities on the page
    cities = City.objects.all() 

    error_message = ''
    message_class = ''

    if request.method == 'POST': 
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name'].capitalize()
            if not City.objects.filter(name=city_name).exists():
                form.save()
                return redirect('index')
            else:
                error_message = 'City already exists!'
                message_class = 'is-danger'

    else:
        form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city, keys.open_weather_api)).json() #request the API data and convert the JSON to Python data types
        temp_in_f = city_weather['main']['temp']
        temp_in_c = (temp_in_f - 32) * 5/9
        feels_like_f = city_weather['main']['feels_like']
        feels_like_c = (feels_like_f - 32) * 5/9

        weather = {
            'city': city_weather['name'].capitalize(),
            'temperature': round(temp_in_c, 1),
            'feels_like': round(feels_like_c, 1),
            'description': city_weather['weather'][0]['description'].capitalize(),
            'recommendation': clothing_recommendations(feels_like_c),
            'icon': city_weather['weather'][0]['icon']
        }
        if weather in weather_data:
            continue
        else:
            weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form, 'error_message': error_message, 'message_class': message_class}

    return render(request, 'weather/index.html', context) #returns the index.html template

def clothing_recommendations(feels_like):
    if feels_like > 30:
        return 'stay inside, keep cool and hydrated!'
    elif feels_like > 25:
        return 'wear something bright, light and airy... and sunscreen!'
    elif feels_like > 20:
        return 'wear something light, maybe shorts and a t-shirt?... and sunscreen!'
    elif feels_like > 17:
        return 'wear a nice t-shirt and light trousers.'
    elif feels_like > 10:
        return 'wear something warm, but unrestrictive.'
    elif feels_like > 0:
        return 'wrap up in a warm coat!'
    elif feels_like < 0:
        return 'stay inside and keep warm by the fire.'