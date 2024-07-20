#imports
import files, hourly, daily
import pandas as pd #type: ignore

def hourly_data(loc):
    lat, long = files.get_coords(loc)
    files.get_forecast(lat, long)
    hours = hourly.get_hours()
    return hours

def daily_data(loc):
    lat, long = files.get_coords(loc)
    files.get_forecast(lat, long)
    days = daily.get_days()
    return days

hours = hourly_data("Edison, NJ")
hours.to_csv("./files/hourData.csv")

days = daily_data("Edison, NJ")
days.to_csv("./files/dayData.csv")