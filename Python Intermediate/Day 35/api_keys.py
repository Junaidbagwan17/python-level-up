import requests

api_key = "0f35c5cd22f0b532bb5d9482065a30d5"
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
MY_LAT = 19.456360
MY_LONG = 72.792458

#just copy after that api url and paste here you will get https like below
# https://api.openweathermap.org/data/2.5/forecast?lat=19.456360&lon=72.792458&appid=0f35c5cd22f0b532bb5d9482065a30d5



parameters = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":api_key
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()

data = response.json()

print(data)