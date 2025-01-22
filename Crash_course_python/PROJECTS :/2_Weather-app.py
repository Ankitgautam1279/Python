import requests
import json
import os
city = input("Enter the name of the city : ")
print("Current Temperature in", city,"is : \t")

url = f"http://api.weatherapi.com/v1/current.json?key=04a77385ba7748f4800172922250901&q={city}&aqi=no"

r = requests.get(url)

# print(r.text)

wdic = json.loads(r.text)
w = (wdic["current"]["temp_c"])
print(wdic["current"]["temp_c"])

os.system(f"say 'The current weather in {city} is {w} degree'")
