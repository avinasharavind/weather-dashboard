#imports
import schedule 
import time
import random
import files, hourly, daily

def hourly_data(loc):
    lat, long = files.get_coords(loc)
    files.get_forecast(lat, long)
    hourly.get_hours()

def daily_data(loc):
    lat, long = files.get_coords(loc)
    files.get_forecast(lat, long)
    daily.get_days()

hourly_data("Ithaca, NY")
daily_data("Ithaca, NY")

