import requests
from pprint import pprint

import self as self

SHEETY_ENDPOINT = "https://api.sheety.co/6d667b22e26be3235b71caebbc2771cf/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/6d667b22e26be3235b71caebbc2771cf/flightDeals/users"

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for i in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": i["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{i['id']}",
                                    json=new_data)
            print(response.text)

    def get_customers_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
