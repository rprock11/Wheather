from django.shortcuts import render
import requests
from django.contrib import messages
from decouple import config


# Create your views here.
def index(request):
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city="kathmandu"
    url_api=config('url_api')    
    image_api=config('image_api')    
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={url_api}"
    param={'units':'metric'}
    data=requests.get(url,param).json()

    img_url=f"https://api.unsplash.com/search/photos?query={city}&per_page=1&client_id={image_api}"
    response=requests.get(img_url).json()
    
    try:
        image=response['results'][0]['urls']['regular']
        temp=data['main']['temp']
        desc=data['weather'][0]['description']
        wind=data['wind']['speed']
        humidity=data['main']['humidity']
        pressure=data['main']['pressure']
        visibility=data['visibility']/1000
        feels_like=data['main']['feels_like']
        min_temp=data['main']['temp_min']
        max_temp=data['main']['temp_max']
        weather_cond=data['weather'][0]['main']
        
    except:
        wind = 0
        humidity = 0
        pressure = 0
        visibility = 0
        feels_like = 0
        min_temp = 0
        max_temp = 0
        weather_cond = 0
        image=None
        temp=0
        desc=city
        messages.error(request,"no such city!!")
    context={'image':image,
        'temp':temp,
        'city':city,
        'desc':desc,
        'wind':wind,
        'humidity':humidity,
        'pressure':pressure,
        'visibility':visibility,
        'feels':feels_like,
        'min':min_temp,
        'max':max_temp,
        'condition':weather_cond,}

    return render(request,'index.html',context)
    
    


