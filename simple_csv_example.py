"""

In this file, we will attempt to read in a simplified 15-record
Real Estate transactions .csv and write the lat/long data to that
file using the Geocoding methods from Geocoding.py

The method is:
Issue HTTP GET Request -> Google Maps API -> Parse JSON Response

We will also do some basic data manipulation and cleaning in pandas.
"""

import pandas as pd
import requests
import json
import numpy as np

df = pd.read_csv("ct_2021_sales_single_family.csv")

df_dtype = df.dtypes

"""
Serial Number         int64
List Year             int64
Date Recorded        object
Town                 object
Address              object
Assessed Value       object
Sale Amount          object
Sales Ratio         float64
Property Type        object
Residential Type     object
Non Use Code         object
Assessor Remarks     object
OPM remarks         float64
Location             object
dtype: object
"""

print(df_dtype, "\n")
print(df, "\n")
shape = df.shape
print(shape)
print(df.shape)
print(df.head)

"""

We would like to:
    1) Load 'Address' and 'Town' variables from .csv
    2) Concatenate as full 'Location' string
    3) Pass 'Location' string through Google Maps API
    4) Read and Save 'Lat' and 'Long' variables into Spreadsheet

"""

#-- Create new column in Pandas
#-- Concatenate 'Address' + 'Town' + CT

df['Location String'] = df['Address'] + " " + df['Town'] + " " + "CT"
print(df['Location String'])

#-- Write a function that will be called with Pandas apply() method to pass
#   location string as API argument and return Latitude, Longitude

def return_lat_long(loc):
    my_address = str(loc)
    separated_address = my_address.replace(" ", "%")
    geocoding_string = ("https://maps.googleapis.com/maps/api/geocode/json?address="
                        + separated_address
                        + "&key=AIzaSyBRfH9tGBT9BVd4EY6T_3r4YJ5UGi4z1dY")
    # print(geocoding_string)

    #-- Pass loaded URL string to requests.GET() method
    try:
        my_geocoded_output = requests.get(geocoding_string)
        #print(my_geocoded_output.text)
        #print(type(my_geocoded_output))
        json_response = my_geocoded_output.json()
        #print(json_response)
        #print('\n')

        if json_response['results']:
            lat = json_response['results'][0]['geometry']['location']['lat']
            lng = json_response['results'][0]['geometry']['location']['lng']
            #print(lat, lng)
            return lat, lng

    except ValueError:
        return np.nan, np.nan


df['LatLong'] = df['Location String'].apply(return_lat_long)
df.to_csv('ct_2021_sales_single_family_latlong.csv')

# df[['Lat', 'Long']] = df['Location String'].apply(return_lat_long)




