import requests
import datetime
import smtplib
import time

my_email = "VinnyThePinny@gmail.com"
password = "ThePinny/300496"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_position = (data["iss_position"]["latitude"], data["iss_position"]["longitude"])
print(iss_position)

params = {
    "lat": 48.856613,
    "lng": 2.352222,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
data = response.json()
print(data)

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
time_now = datetime.datetime.now()
print(time_now.hour)
print(f"{sunrise}\n{sunset}")

while True:
    time.sleep(60)
    if params["lat"] - 5 <= float(iss_position[0]) <= params["lat"] + 5:
        if params["lng"] - 5 <= float(iss_position[1]) <= params["lng"] + 5:
            if float(sunrise) >= time_now.hour or float(sunset) <= time_now.hour:
                with smtplib.SMTP("smtp.gmail.com") as mail:
                    mail.starttls()
                    mail.login(my_email, password)
                    mail.sendmail(from_addr=my_email, to_addrs="vincentbaron1996@gmail.com",
                                  msg="Subject: CHECK FOR THE ISS\n\n UP IN THE SKY")

