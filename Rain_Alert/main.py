import requests
from twilio.rest import Client
import os

api_key = os.environ.get("OWM_API_KEY")
account_sid = "ACb30b41a896db509636494254ad27bd14"
auth_token = os.environ.get("AUTH_TOKEN")

params = {
    "lat": 26.38,
    "lon": 163.9,
    "appid": "cbe214e644b897fdb59d5d361a6f6c52",
    "exclude": "current,minutely,daily"
}

api = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=params)
api.raise_for_status()
data = api.json()
weather = data["hourly"][0]["weather"][0]["id"]
print(weather)
will_rain = False

i = 0
while i < 12:
    if data["hourly"][i]["weather"][0]["id"] < 700:
        will_rain = True
    i += 1
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Il va pleuvoir aujourd-huis Victoire, n'oublies pas ton parapluie. Bisous.😘☔",
        from_='+15613366563',
        to='+33695143200'
    )
    print(message.status)
