from data_mangager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Create objects
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()


# Get spreadsheet data
sheet_data = data_manager.get_destination_data()

# Loop through every city
for city_data in sheet_data:

    city = city_data["city"]
    iata_code = city_data["iataCode"]
    lowest_price = city_data["lowestPrice"]

    flight = flight_search.check_flights(destination_city=city, destination_airport=iata_code)

    message = f"""Cheap Flight Alert! ✈️

Destination: {flight.destination_city}
Airport: {flight.destination_airport}

Price: £{flight.price}

Departure: {flight.out_date}
Return: {flight.return_date}
"""

    # Comparison logic
    if flight.price < lowest_price:
        notification_manager.send_message(message=message)

    # Print details
    print(
        f"{flight.destination_city} - "
        f"{flight.destination_airport} - "
        f"{flight.price} - "
        f"Departure: {flight.out_date} - "
        f"Return: {flight.return_date}"
    )

