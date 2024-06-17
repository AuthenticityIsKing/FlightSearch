from twilio.rest import Client
import os
import load_dotenv
load_dotenv.load_dotenv()

TRIAL_NUMBER = os.environ['TRIAL_NUMBER']
PERSONAL_NUMBER = os.environ['PERSONAL_NUMBER']

## meant to send text messages based on info fed it from main.py
class NotificationManager:
    def __init__(self, sid, token):
        self.client = Client(sid, token)

    def message(self, iataOne, iataTwo, dateOne, dateTwo, price):
        message = (self.client.messages.create(
            body=f"Flight from {iataOne} to {iataTwo}, {dateOne} to {dateTwo}, and it costs {price} pounds",
            from_=TRIAL_NUMBER,
            to=PERSONAL_NUMBER))
