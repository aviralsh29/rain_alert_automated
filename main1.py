import requests
import os
import smtplib
from datetime import datetime
day = datetime.now()
weekday = day.weekday()
email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")
api_key= os.environ.get("API_KEY")
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params={
    "lat":28.616239 , "lon":77.374005,"appid":api_key,"cnt":3
})
response.raise_for_status()
data = response.json()

will_rain = False
for item in data["list"]:
     condition_code= item["weather"][0]["id"]
     if int(condition_code) <700 and weekday not in (5,6):
         will_rain= True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email,password)
        connection.sendmail(to_addrs=os.environ.get("SENDING_EMAIL"),from_addr= email, msg="Subject:ITS GOING TO RAIN BRING AN UMBRELLA\n\nbring an umbrella please")