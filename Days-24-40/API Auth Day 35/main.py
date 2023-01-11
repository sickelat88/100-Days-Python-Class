import requests
import os

# https://api.openweathermap.org/data/2.5/forecast?lat=35.583710&lon=-78.800850&appid=8654f8474c9e9d2fe28254be3709229d
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""
#env
#export OWM_API_KEY="xxx"
#api_key = os.environ.get("OWM_API_KEY")

params = {
    "lat": 35.583710,
    "lon": -78.800850,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

is_hot = False

response = requests.get(OWM_endpoint, params=params)
response.raise_for_status()
weather = response.json()
weather_slice = weather["list"][0:12]
for hour_data in weather_slice:
    temp = hour_data["main"]["temp"]
    if temp > 280:
        is_hot = True
if is_hot:
    print("It's hot")






