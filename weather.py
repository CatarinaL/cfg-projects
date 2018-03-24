import requests
from datetime import date, timedelta
import pprint
pp = pprint.PrettyPrinter(indent=4)

to_day = date.today()
five_days = timedelta(days=5)
forecast = to_day + five_days

print(forecast.isoformat())

#"http://api.openweathermap.org/data/2.5/weather" -> current weather
endpoint = "http://api.openweathermap.org/data/2.5/forecast"
payload = {"q": "Dublin", "units":"metric", "forecast.time.from":to_day, "forecast.time.to":five_days, "appid":"607dd6fab965f1b464e44f1f529548d2"}
response = requests.get(endpoint, params=payload)
print(response.url)
#print(response.status_code)
#print(response.headers["content-type"])
info_response = response.json()
#pp.pprint(info_response) #pretty print
#pp.pprint(info_response['list'][0]['main'])
count = info_response['cnt'] #count, hopefully
main_list = info_response['list'][0]['main']
pp.pprint(main_list['humidity'])
humidity = main_list['humidity']
#print(info_response['main']['temp'])

for i in range(0, count):
    print(info_response['list'][i]['dt_txt'])
    print(info_response['list'][i]['main']['humidity'])


humidity_list = []
for i in range(0, count):
    humidity_list.append(info_response['list'][i]['main']['humidity'])



humidity_date_dict = {}
for item_at_index in info_response['list']:
    humidity_date_dict["humidity"] = item_at_index['main']['humidity']
    humidity_date_dict["date"] = item_at_index['dt_txt']

print(humidity_date_dict) #redo this: make dictionary with key-date:value:humidity
