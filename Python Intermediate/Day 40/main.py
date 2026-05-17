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

    # Search flight
    flight = flight_search.check_flights(
        destination_city=city,
        destination_airport=iata_code
    )

    # Create message
    message = f"""Cheap Flight Alert! ✈️

Destination: {flight.destination_city}
Airport: {flight.destination_airport}

Price: £{flight.price}

Departure: {flight.out_date}
Return: {flight.return_date}
"""

    # Comparison logic
    if flight.price < lowest_price:

        # Telegram alert
        notification_manager.send_message(message=message)

        # Get all customers
        customers = data_manager.get_customer_emails()

        # Send emails to all customers
        for customer in customers:
            notification_manager.send_email(user_email=customer["email"],sendemail_alert=message)

    # Print details in terminal
    print(
        f"{flight.destination_city} - "
        f"{flight.destination_airport} - "
        f"{flight.price} - "
        f"Departure: {flight.out_date} - "
        f"Return: {flight.return_date}"
    )


# ---------------- USER SIGNUP ---------------- #

def user_signup():

    print("Welcome to Junaid's Flight Club.")
    print("We find the best flight deals and email you.\n")

    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    user_email = input("What is your email?\n")
    confirm_email = input("Type your email again:\n")

    if user_email == confirm_email:
        print("You are in the club!")

        data_manager.add_user(
            first_name=first_name,
            last_name=last_name,
            user_email=user_email
        )

    else:
        print("Emails do not match.")

# Run signup system
user_signup()