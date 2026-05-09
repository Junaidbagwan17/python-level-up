import requests
import smtplib
import os
# ---------------- WEATHER API ---------------- #
my_email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]
api_key = os.environ["API_KEY"]

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'

MY_LAT = 19.456360
MY_LONG = 72.792458

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "units": "metric"
}
response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

# ---------------- CHECK WEATHER ---------------- #

# Check next 5 forecast blocks
# (roughly whole daytime if script runs in morning)
weather_slice = weather_data["list"][0:5]

will_rain = False
for forecast in weather_slice:
    condition_code = forecast["weather"][0]["id"]
    rain_probability = forecast["pop"]
    print(forecast["dt_txt"])
    print("Condition Code:", condition_code)
    print("Rain Probability:", rain_probability)
    print("----------------------")

    # Rain condition
    if condition_code < 700 or rain_probability > 0.3:
        will_rain = True

# ---------------- SEND EMAIL ---------------- #
if will_rain:

    subject = "Bring an Umbrella ☔"
    body = """
            It may rain today.

            Please carry:
            - Umbrella or raincoat
            - Water bottle
            - Safe footwear

            Travel safely and avoid rushing on platforms.

            Have a safe office journey 🌧️
            """
    message = f"Subject:{subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(
            user=my_email,
            password=password
        )
        connection.sendmail(
            from_addr=my_email,
            to_addrs="miraroadauto@gmail.com",
            msg=message.encode("utf-8")
        )
    print("Rain alert email sent ☔")
else:
    print("No rain expected today ☀️")

