import json
import re
from django.shortcuts import render
import requests
import datetime
from django.contrib import messages

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Pune'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e86d313cd350cc88b11d2a12b51a4107'
    PARAMS = {'units':'metric'}

    print("Searching for {} city >>>>>>>>>>>>>>>>>>>>>>".format(city))
    API_KEY = 'AIzaSyDg1c_2YNGthWrPvOdw-MYgxc4A4V-KrL8'

    SEARCH_ENGINE_ID = '90365d3c870944530'

    query = city + "1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    
    # print(data)
    count = 1
    search_items = data.get("items")
    

    try:
        image_url = search_items[0]['link']
        # print(image_url.split())
        print(image_url.split('.')[-1])
        data = requests.get(url, PARAMS,  verify=False).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        day = datetime.date.today()

        for i in ['jpg', 'jpeg', 'png']:
            if i in image_url:
                break
        else:
            image_url = 'https://images.pexels.com/photos/3008509/pexels-photo-3008509.jpeg?auto=compress&cs=tinysrgb&w=1600'
        return render(request, 'index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city,'exception_occurred':False,'image_url':image_url})

    except:
        exception_occurred = True
        messages.error(request,'entered data is not available to API') 
        day=datetime.date.today()   

        return render(request, 'index.html',{'description':'clear sky','icon':'01d','temp':25,'day':day,'city':city,'exception_occurred':exception_occurred})