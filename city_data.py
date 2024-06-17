import requests, pprint


## processes data amadeus provides about each city
amadeus_link = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
sheety_link = YOUR SHEETY LINK HERE
sheety_edit = YOUR SHEETY LINK EDIT LINK HERE
sheet_data = requests.get(url=sheety_link).json()

class CityData:
    def __init__(self, city, headers):
        self.city = city
        self.header = headers


    def findGeneralData(self):
        param = {"keyword": self.city,
                 "include": ["AIRPORTS"]}
        return requests.get(url=amadeus_link, params=param, headers=self.header).json()

    def dataIATA(self):
        return self.findGeneralData()['data'][0]['iataCode']

    def populateIATA(self):
        for n in sheet_data["prices"]:
            params = {"price": {"iataCode": self.dataIATA()}}
            requests.put(url=sheety_edit + str(n["id"]), json=params)

