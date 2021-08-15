import requests
from pprint import pprint


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.sheety_endpoint = 'https://api.sheety.co/7d415d13c97ec10235f431bbbf3f67a5/flightDeals/prices'
        response = requests.get(url=self.sheety_endpoint)
        self.data = response.json()
