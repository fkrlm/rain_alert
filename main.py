import requests
import datetime as dt
from twilio.rest import Client

account_sid = 'ACd77dc6696899218fa0cc976bf05813e2'
auth_token = '0c78f99a5fef30de00133c61ed8d647e'
api_key = '0a9346580256ecf37a054ffb21afc25e'
# end_point = "https://api.openweathermap.org/data/2.5/weather"
# parameters = {"q": "Alexandria,US", "appid": "0a9346580256ecf37a054ffb21afc25e"}
# # ?q=Alexandria,US&appid=0a9346580256ecf37a054ffb21afc25e
# response = requests.get(url=end_point, params=parameters)
# response.raise_for_status()
# data = response.json()

# Call 5 day / 3-hour forecast data
# How to make an API call
# https://api.openweathermap.org/data/2.5/forecast?lat=38.80&lon=-77.01&appid=0a9346580256ecf37a054ffb21afc25e
EWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": 38.80,
    "lon": -77.01,
    "appid": api_key
}
response = requests.get(url=EWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

# using range
# for x in range(40):
#     code = data["list"][x]["weather"][0]["id"]
#     if code < 700:
#         three_hours_datatime = data["list"][x]["dt"]
#         date_time = dt.datetime.fromtimestamp(three_hours_datatime)
#         print(f"You need to have an umbrella at {date_time} time!")


# Using slice
weather_slice = weather_data["list"][:40]

will_rain = False

for three_hour_data in weather_slice:
    condition_code = three_hour_data["weather"][0]["id"]
    three_hours_datatime = three_hour_data["dt"]
    date_time = dt.datetime.fromtimestamp(three_hours_datatime)
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"It is going to run at {date_time} time. Remember to bring an umbrella🦌!",
        from_='+13392448916',
        to='+15712680154'
    )
    print(message.status)
# test