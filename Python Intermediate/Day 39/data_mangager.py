import requests

class DataManager:
    def __init__(self):
        self.SHEETY_Endpoint = "YOUR ENDPOINT"

    def get_destination_data(self):
        response = requests.get(url=self.SHEETY_Endpoint)
        data = response.json()
        return data["prices"]

