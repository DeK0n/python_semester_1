import requests
import json

request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
print("Here is a joke:")
print(response['value'])
