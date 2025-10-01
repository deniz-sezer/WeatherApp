from urllib import request as urlrequest
import json
from django.shortcuts import render
from django.conf import settings

def home(request):
    weather = None
    city = request.GET.get("city")
    
    if city:
        api_key = settings.OPENWEATHER_KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=en"
        
        try:
            with urlrequest.urlopen(url) as response:
                data = json.load(response)
            
            if data.get("cod") == 200:
                weather = {
                    "city": data["name"],
                    "weather": data["weather"][0]["description"],
                    "temp": data["main"]["temp"],
                    "humidity": data["main"]["humidity"]
                }
            else:
                weather = {
                    "city": city,
                    "weather": "Not found",
                    "temp": "-",
                    "humidity": "-"
                }
        except:
            weather = {
                "city": city,
                "weather": "Error fetching data",
                "temp": "-",
                "humidity": "-"
            }
    
    return render(request, "weather/index.html", {"weather": weather})

