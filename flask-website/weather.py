import requests

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "Dublin", "units":"metric", "appid":"607dd6fab965f1b464e44f1f529548d2"}
response = requests.get(endpoint, params=payload)
print response.url
print response.status_code
print response.headers["content-type"]
