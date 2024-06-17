# FlightSearch

Based on the Day 39 project of the Udemy Course "100 Days of Code: The Complete Python Pro Bootcamp"
The idea and guidance provided by Udemy Course "100 Days of Code: The Complete Python Pro Bootcamp" by Dr. Angela Yu

This program is meant to find the cheapest flights from London to any of the places in the spreadsheet (again provided by Dr. Yu and London App Brewery) below:

https://docs.google.com/spreadsheets/d/1YMK-kYDYwuiGZoawQy7zyDjEIU9u8oggCV4H2M9j7os/edit?gid=0#gid=0 

It accesses the Google Sheet through the API Sheety, populates IATA codes, finds flights, and prices through Amadeus, 
and uses Twilio to send text messages to notify the user of deals that may occur. 

To use said program, all one needs to do is sign up with Amadeus, Sheety, and Twilio respectively, get their Sheety URL as well as tokens/keys/secrets from Amadeus and Twilio, and put these values in the appropriate variables.
