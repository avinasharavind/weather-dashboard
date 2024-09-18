import json
import statistics

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
    if int(item["startTime"][-14:-12]) > 10 and int(item["startTime"][-14:-12]) < 18:
        humlist.append(item["relativeHumidity"]["value"])
print(f'The Max Daytime RH is {max(humlist[:period])}% ("Daytime" is 11am-5pm)')
print(f'The Min Daytime RH is {min(humlist[:period])}% ("Daytime" is 11am-5pm)')

#max/min windspeed
windlist = []
for item in hours:
    windlist.append(item["windSpeed"])
print(f'The Max Wind Speed is {max(windlist[:period])}')

#most common weather
weatherlist = []
for item in hours:
    weatherlist.append(item["shortForecast"])
print(f'The most frequent weather type is is {statistics.mode(weatherlist[:period])}')

print("\n")