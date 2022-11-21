import requests
import json
cityName = input("Enter city name: ")
request = "https://api.openweathermap.org/data/2.5/weather?q=" + \
    cityName+"&appid={APIkey}&units=metric" # paste your openweathermap api key where {APIkey} without brackets
response = requests.get(request).json()
print(response)
print("Weather conditions in "+str(cityName)+": ")
print(str(response["weather"][0]["description"])+" and "+ str(response["main"]["temp"])+" C")

