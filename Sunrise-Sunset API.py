import requests
import datetime

#Give parameter To Your own Location
parameter = {
    'lat':26.650110,
    'lng':84.901779,
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
response.raise_for_status()

view = response.json()

time_now = datetime.datetime.now()


print('Todays Date :' ,time_now.date())
print('Todays Time :' ,time_now.strftime('%I:%M:%S %p'))


# print(view)
print('Sunrise     :', view['results']['sunrise'])
print('Sunset      :', view['results']['sunset'])
print('Day length  :', view['results']['day_length'])