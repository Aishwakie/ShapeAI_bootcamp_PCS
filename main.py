import requests
from datetime import datetime

api_key='2729b6bf1ec97e5d65a13866d7ce5442'
location=input("Enter the city name: ")

complete_api_link="https://api.openweathermap.org/date/2.5/weather?q="+location+"&appid="+api_key
api_link=requests.get(complete_api_link)
api_data=api_link.json()

temp_city=((api_data['main']['temp'])-273.15)
weather_desc=api_data['weather'][0]['description']
hmdt=api_data['main']['humidity']
wind_spd=api_data['wind']['speed']
date_time=datetime.now().strftime("%d %b %Y || %I:%M:%S %p")

print("---------------------------------------------")
print("Weather status for -{} || {}".format(location.upper(),date_time))
print("---------------------------------------------")

print("Current temperature is:{:.2f} deg C".format(temp_city))
print("Current weather desc:",weather_desc)
print("Current humidity:",hmdt,'%')
print("Current wind speed:",wind_spd,'kmph')

