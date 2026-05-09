import requests
import smtplib

api_key = "0f35c5cd22f0b532bb5d9482065a30d5"
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
MY_LAT = 19.456360
MY_LONG = 72.792458

parameters = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":api_key,
    "units":"metric"
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)
# print(weather_data["list"][3]["weather"][0]['id']) # but how can we get for other hours?

weather_slice = weather_data["list"][4:10] #6am to 9pm
will_rain = False

for forecast in weather_slice:
    condition_code = forecast["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain =True

if will_rain:
    print("Bring an Umbrella")
# send mail
    my_email = "ml.technologia2026@gmail.com"
    password = "bhjf dtsl ieaj xgyx"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="miraroadauto@gmail.com",
                            msg="Subject:Bring an Umbrella☔\n\n It may rain so please dont forget to bring raincoat"
                                " or umbrella! also book a train ticket before leaving home. "
                                "and be hydrated wear rainy footwear and avoid running on platforms\n "
                                "\n Don't rush; there are many trains, but only one life."
                                "\n \nIt's quite a storm out there! Wishing you a smooth and safe journey to the office today." .encode("utf-8")
                            )
