import requests
sheety_link = "https://api.sheety.co/4ba8e6f99a2ffd07ec64164735a79d4c/copyOfFlightDeals/prices"

## meant to process info from the google sheet (accessed by the sheety api) in ways for flight_search to process easily
class DataManager:
    def __init__(self):
        self.cities = []
        self.iata = []
        self.prices = {}
        city = requests.get(url=sheety_link).json()
        city = city['prices']
        for info in city:
            self.cities.append(info["city"])
            self.iata.append(info["iataCode"])
            self.prices[info["iataCode"]] = info["lowestPrice"]






