#imports
import schedule 
import time
import random
import files, hourly, daily

def hourly_data(loc):
    lat, long = files.get_coords(loc)
    files.get_forecast(lat, long)
    hourly.get_hours()
    print(time.time())

def daily_data(loc):
    lat, long = files.get_coords(loc)
    files.get_forecast(lat, long)
    daily.get_days()


schedule.every(30).minutes.at(":"+str(random.randint(10,45))).do(hourly_data, loc="Edison, NJ")
schedule.every(30).minutes.at(":"+str(random.randint(10,45))).do(daily_data, loc="Edison, NJ")


while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute