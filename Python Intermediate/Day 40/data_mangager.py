import requests

class DataManager:
    def __init__(self):
        self.SHEETY_Endpoint = "https://api.sheety.co/4b5e176d3148cc5fcc899a3cb6b134fa/flightDeals/prices"
        self.USERS_Endpoint = "https://api.sheety.co/4b5e176d3148cc5fcc899a3cb6b134fa/flightDeals/users"

    def get_destination_data(self):
        response = requests.get(url=self.SHEETY_Endpoint)
        data = response.json()
        return data["prices"]

    def add_user(self, first_name, last_name, user_email):

        new_user = {
            "user":{
                "firstName": first_name,
                "lastName": last_name,
                "email": user_email
            }
        }

        response = requests.post(url=self.USERS_Endpoint, json=new_user)
        print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.USERS_Endpoint)
        data = response.json()
        return data["users"]
