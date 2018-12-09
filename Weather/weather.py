#!/usr/bin/env python3
import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?appId=5d3d6848798ca04de7a45067fb0551a4&q='
city = input("City Name :")

url = api_address + city

json_data = requests.get(url).json()

print(json_data)
