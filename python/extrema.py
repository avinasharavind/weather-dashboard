import json, statistics, time
import data
import numpy as np

data.job()
time.sleep(10)

hourly = json.load(open("/Users/avinasharavind/Documents/Weather_Projects/NWS_Forecast_Page/static/files/hourly.json"))
hours = hourly["properties"]["periods"]
period = 24*7

print("\n")

#max pops
rainlist = []
for item in hours:
    rainlist.append(item["probabilityOfPrecipitation"]["value"])

print(f'The Max PoPs is {max(rainlist[:period])}%')

#max/min temp
templist = []
for item in hours:
    templist.append(item["temperature"])
print(f'The Max Temperature is {max(templist[:period])}F')
print(f'The Min Temperature is {min(templist[:period])}F')

#max/min daytime rh
humlist = []
for item in hours:
    if int(item["startTime"][-14:-12]) > 12 and int(item["startTime"][-14:-12]) < 19:
        humlist.append(item["relativeHumidity"]["value"])
print(f'The Max Midday RH is {max(humlist[:period])}% ("Midday" is 12pm-6pm)')
print(f'The Min Midday RH is {min(humlist[:period])}% ("Midday" is 12pm-6pm)')

#max/min windspeed
windlist = []
for item in hours:
    windlist.append(item["windSpeed"])
print(f'The Max Wind Speed is {max(windlist[:period])}')

#most common weather
weatherlist = []
for item in hours:
    weatherlist.append(item["shortForecast"])
weathermode = statistics.mode(weatherlist[:period])
print(f'The most frequent weather type is is {weathermode}')

print("\n")