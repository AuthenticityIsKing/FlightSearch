
import data_manager
import requests
amadeus_link = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    def __init__(self, headersForAmadeus):
        data = data_manager.DataManager()
        self.cities = data.cities
        self.iata = data.iata
        self.comparison = data.prices
        self.cheapest = {}
        self.header = headersForAmadeus

    def findCheapest(self, beginningTime, endTime):
        cheapest = []
        for destination in self.iata:
            ##accessing results for each destination
            data = {
                "originLocationCode": "LON",
                "destinationLocationCode": destination,
                "departureDate": beginningTime.strftime("%Y-%m-%d"),
                "returnDate": endTime.strftime("%Y-%m-%d"),
                "adults": "1",
                "max": str(self.comparison[destination])
            }
            works = False

            cheap = requests.get(url=amadeus_link, params=data, headers=self.header).json()

            ## meant to evaluate if amadeus has given results.
            try:
                cheap['data']
                works = True
            except:
                works = False
            if works:
                d = [] ##stores the relevant info from all the flights the amadeus returns.
                for n in cheap["data"]:
                    infoHome = n["itineraries"][0]["segments"][0]['departure']
                    infoDestination = n["itineraries"][1]["segments"][0]['departure']
                    #stores destination general IATA code, departure date to destination, departure date from destination, IATA code for place of origin, IATA code for destination, and price (in this order)
                    d.append([destination, infoHome['at'], infoDestination['at'], infoHome['iataCode'], infoDestination['iataCode'], n['price']['total']])
                max = d[0][4]
                index = 0
                for i in range(len(d)):
                    if d[i][4] < max:
                        index = i
                        max = d[i][4]
                cheapest.append(d[index])
        return cheapest





