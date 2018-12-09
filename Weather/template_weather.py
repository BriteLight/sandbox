#!/usr/bin/env python3
import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?appId=<auth-app-id>&q='
city = input("City Name :")

url = api_address + city

json_data = requests.get(url).json()

print(json_data)
