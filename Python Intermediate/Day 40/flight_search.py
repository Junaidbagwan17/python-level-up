import random
from flight_data import FlightData
from datetime import timedelta, datetime

class FlightSearch:
    def check_flights(self,  destination_city, destination_airport):

        price = random.randint(10, 1000)
        origin_city = "London"
        origin_airport = "LON"

        tomorrow = datetime.now() + timedelta(days=1) #current date + 1 day
        return_date = tomorrow + timedelta(days=7)

        out_date  = tomorrow.strftime("%Y-%m-%d")
        return_date = return_date.strftime("%Y-%m-%d")
        flight_data = FlightData(
            price = price,
            origin_city = origin_city,
            origin_airport = origin_airport,
            destination_city = destination_city,
            destination_airport = destination_airport,
            out_date = out_date,
            return_date = return_date,

        )
        return flight_data
