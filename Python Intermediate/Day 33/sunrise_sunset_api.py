import requests
from datetime import datetime

my_lat = 19.458380
my_long= 72.767639

parameters  = {
    "lat":my_lat,
    "lng":my_long,
    "formatted":0
}
response= requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print("SUNRISE UTC:", sunrise)
print("SUNSET UTC :",sunset)

time_now = datetime.now()
print("Time NOW:", time_now.hour)
