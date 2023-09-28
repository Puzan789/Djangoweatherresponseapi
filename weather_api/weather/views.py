from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def index(request):
    API_KEY="5abe27c25025f97ef845d04b93985a47"
    API_URL=f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API_KEY}"
    try:
        r= requests.get(API_URL)
        if r.status_code == 200:
            weather_data=r.json()

            return render(request,'weather/weather.html',{"weather":weather_data})
        else:
            errormessage=f"ERROR: {r.status_code}-{r.status_text}"
            return render(request,'weather/weather.html',{"errormessage":errormessage})
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        context = {
            'error_message': error_message,
        }
        return render(request, 'weather/error.html', context)
      




