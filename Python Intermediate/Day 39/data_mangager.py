import requests

class DataManager:
    def __init__(self):
        self.SHEETY_Endpoint = "https://api.sheety.co/4b5e176d3148cc5fcc899a3cb6b134fa/flightDeals/prices"

    def get_destination_data(self):
        response = requests.get(url=self.SHEETY_Endpoint)
        data = response.json()
        return data["prices"]

