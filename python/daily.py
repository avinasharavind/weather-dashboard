#imports
import json
import pandas as pd  # type: ignore
import time

def get_days():
    #Gets daily (Day/Night) data from forecast.json
    outlook = json.load(open("./files/forecast.json"))

    periods = []
    for ts in outlook["properties"]["periods"]:
        info = []
        info.append(ts["name"])
        info.append(ts["isDaytime"])
        info.append(ts["temperature"])
        info.append(ts["probabilityOfPrecipitation"]["value"])
        info.append(ts["windSpeed"])
        info.append(ts["windDirection"])

        string = ts["icon"]
        string = string.split("/")
        string = string[-1]
        string = string.split("?")
        string = string[0]
        string = string.split(",")
        string = string[0]
        info.append(string)

        info.append(ts["detailedForecast"])
        periods.append(info)

    periods = pd.DataFrame(data=periods, columns=["name", "isDay", "Temp", "PoPs", "wdSpd", "wdDir", "icon", "longFcst"])

    return periods