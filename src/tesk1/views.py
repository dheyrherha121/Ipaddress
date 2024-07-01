from django.shortcuts import render
from requests import get

# Create your views here.
def hello(request):
    visitor_name=request.GET.get('Visitor_name', 'visitor_name')
#for loction 
    loc= get('https://ipapi.co/json/')
    loc_data=loc.json()
    location=loc_data.get("city")
    client_ip=loc_data.get("ip")

    #for the temp 
    api_key = "43155ad1b40cf402395c590aab20fac1"
    base_url =  "http://api.openweathermap.org/data/2.5/weather/?"
    complete_url=f"{base_url}q={location}&appid={api_key}&units=metric"
    response=get(complete_url).json()
    temp=response['main']['temp']

    return {'client_ip':client_ip,'location':location, 'greeting':f'hello {visitor_name}!,the temperature is {temp} degree Celsius in {location} '}
