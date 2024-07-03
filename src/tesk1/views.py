from requests import get
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
from django.http import HttpResponse

def hello(request):
   
    visitor_name= request.GET.get('visitor_name')
    
    client_ip=request.META.get('REMOTE_ADDR')
    token= '1b6a79055dd6a8'
    ip_url=get(f"https://ipinfo.io/{client_ip}/city/json?token={token}").json()
    #ip=ip_url.get("ip")
    city=ip_url.get("city")

    api_key = "43155ad1b40cf402395c590aab20fac1"
    base_url =  "http://api.openweathermap.org/data/2.5/weather/?"
    complete_url=f"{base_url}q={city}&appid={api_key}&units=metric"
    response=get(complete_url).json()
    temp=response['main']['temp']

    response= {'client_ip':client_ip,'location':city, 'greeting':f'hello {visitor_name}!,the temperature is {temp} degree Celsius in {city} '}
    return JsonResponse(response)



    
