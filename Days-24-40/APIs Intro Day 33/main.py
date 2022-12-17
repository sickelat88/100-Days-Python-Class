import requests
from datetime import datetime

MY_LAT = 35.583710
MY_LONG = -78.800850

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# coords = (longitude, latitude)
#
# print(coords)

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

time_now = datetime.now()

print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])
print(time_now.hour)

