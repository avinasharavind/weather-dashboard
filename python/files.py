"""
Opens the required files to get forecast information from the National Weather Service API. 
Created by Avinash Aravind
"""

#imports
import requests
import xml.etree.ElementTree as ET
from geopy.geocoders import Nominatim
import json


#Gets and store location info from OSM/Nominatim
loclist = ["Edison, NJ", "Ithaca, NY"]
latlist = [40.518157, 42.44]
longlist = [-74.4113926, -76.495]

def get_coords(loc):
    """
    Gets the coordinates of an input location string using geopy and OpenStreetMap's Nominatim API.
    Parameters:
        loc (str): The input location fetched from the message.
    Returns:
        lat (float): The latitude of the input location, in degrees.
        long (float): The longitude of the input location, in degrees
        (returned as a tuple)
    """
    if loc in loclist:
        idx = loclist.index(loc)
        lat = latlist[idx]
        long = longlist[idx]
    else:
        geolocator = Nominatim(user_agent="fcstpge")
        location = geolocator.geocode(loc)
        lat, long = location.latitude, location.longitude
        loclist.append(loc)
        latlist.append(lat)
        longlist.append(long)
    return lat, long

def get_forecast(lat, long):
    """
    Gets the .json files for the Location, NWS Office, Forecast, Hourly, and Grid Data information for the given location. 
    Parameters:
        lat (float): The latitude of the input location, in degrees.
        long (float): The longitude of the input location, in degrees
    Returns:
        nothing
    """

    url = f"https://api.weather.gov/points/{lat},{long}"
    response = requests.get(url)
    open("./static/files/location.json", "wb").write(response.content)

    f = open("./static/files/location.json")
    data = json.load(f)
    properties = data["properties"]
    forecast = properties["forecast"]
    office = properties["forecastOffice"]
    hourly = properties["forecastHourly"]
    griddata = properties["forecastGridData"]

    office_page = requests.get(office)
    open("./static/files/office.json", "wb").write(office_page.content)
    
    forecast_page = requests.get(forecast)
    open("./static/files/forecast.json", "wb").write(forecast_page.content)

    hourly_page = requests.get(hourly)
    open("./static/files/hourly.json", "wb").write(hourly_page.content)

    griddata_page = requests.get(griddata)
    open("./static/files/griddata.json", "wb").write(griddata_page.content)

