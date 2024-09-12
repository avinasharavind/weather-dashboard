#imports
import files, hourly, daily
import schedule, time

def hourly_data(loc):
    lat, long = files.get_coords(loc)
    files.get_forecast(lat, long)
    hourly.get_hours()

def daily_data(loc):
    lat, long = files.get_coords(loc)
    files.get_forecast(lat, long)
    daily.get_days()

def job():
    hourly_data("Ithaca, NY")
    daily_data("Ithaca, NY")

schedule.every().hour.at(":05").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

#job()
