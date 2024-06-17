import os
import requests
import flight_search
import datetime
import notification_manager
import load_dotenv
load_dotenv.load_dotenv()

AMADEUS_LINK = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
AMADEUS_SECRET = os.environ['AMADEUS_SECRET']
AMADEUS_KEY = os.environ['AMADEUS_KEY']
TOKEN_LINK = "https://test.api.amadeus.com/v1/security/oauth2/token"

HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}
DATA = {
        "grant_type": "client_credentials",
        "client_id": AMADEUS_KEY,
        "client_secret": AMADEUS_SECRET
}

TWILIO_SID = os.environ["TWILIO_SID"]
TWILIO_TOKEN = os.environ['TWILIO_TOKEN']

token = requests.post(url=TOKEN_LINK, headers=HEADERS, data=DATA).json()
headers = {"Authorization": f"Bearer {token["access_token"]}"}

##amadeus asks for a new token that's produced every 30 minutes using secret and key they give.

n = flight_search.FlightSearch(headersForAmadeus=headers)
x = datetime.datetime.now()
y = x + datetime.timedelta(days=1) ##datetime string that represents tomorrow
z = x + datetime.timedelta(days=180) ##datetime string that represents a date six months from now
cheapestFlights = n.findCheapest(beginningTime=y, endTime=z)
print(cheapestFlights)


def sendTexts(): ## send texts to your phone
        noti = notification_manager.NotificationManager(sid=TWILIO_SID, token=TWILIO_TOKEN)
        for flight in cheapestFlights:
                a = noti.message(iataOne=flight[3],
                                 iataTwo=flight[4],
                                 dateOne=flight[1][:10], ##slicing the time string fed by FlightSearch to isolate the date
                                 dateTwo=flight[2][:10], ##same here
                                 price=flight[5])