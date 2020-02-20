# Import all required packages
import requests
import json
import sys
import depend_constant

sys.path.append('../pylib')
from db import mysql


# Generate the sql insert statements
def insert_data2station(api_key_jcd, contract_jcd="dublin"):
    # Get data from JCDecaux
    response = requests.get(
        "https://api.jcdecaux.com/vls/v1/stations?contract=" + contract_jcd + "&apiKey=" + api_key_jcd)

    if response.status_code == 200:
        # Put the json data into a python dict
        data = json.loads(response.text)
        # Id generator
        query = []
        for dict in data:
            # sql += "INSERT INTO station(sid, station_id, station_name, station_address, lat, lng, bike_stands,ava_bikes,ava_stands,status,update_time) " \
            #        "VALUES(NULL,'%i','%s','%s','%f','%f','%i','%i','%i','%s','%i');" % \
            query.append([dict['number'], dict['name'], dict['address'], dict['position']['lat'],
                          dict['position']['lng'], dict['bike_stands'], dict['available_bikes'],
                          dict['available_bike_stands'], dict['status'], (dict['last_update'] / 1000)])
        return query
    else:
        raise Exception("Bad connection.")


def insert_data2weather(lat, lon, sid, station_id, api_key_ow):
    # # Get data from OpenWeather
    ow_response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + api_key_ow)

    if ow_response.status_code == 200:
        # Put the json data into a python dict
        data = json.loads(ow_response.text)
        # sql += "INSERT INTO station_weather(id,station_id,lat,lng,weather_id,temp, " \
        #        "feels_like, temp_min, temp_max, pressure, humidity, wind_speed, " \
        #        "wind_deg, clouds, rain_1h, rain_3h, snow_1h, snow_3h, update_time, sid)" \
        #        "VALUES(NULL,'%i','%f','%f','%i','%.2f','%.2f','%.2f','%.2f','%i','%i','%.2f','%i','%i','%.2f','%.2f','%.2f','%.2f','%i', %i);" % \
        query = [[station_id, lat, lon, data["weather"][0]["id"], data["main"]["temp"] - 273.15,
                  data["main"]["feels_like"] - 273.15, data["main"]["temp_min"] - 273.15,
                  data["main"]["temp_max"] - 273.15, data["main"]["pressure"], data["main"]["humidity"],
                  data["wind"]["speed"], data["wind"]["deg"], data["clouds"]["all"],
                  data.get("rain", dict()).get('1h', 0), data.get("rain", dict()).get('3h', 0),
                  data.get("snow", dict()).get('1h', 0), data.get("snow", dict()).get('3h', 0), data["dt"], sid]]
        return query
    else:
        raise Exception("Bad connection.")


def main():
    # Get the sql query
    query_insert_station = "INSERT INTO station (sid, station_id, station_name, station_address, lat, lng, bike_stands," \
                           "ava_bikes,ava_stands,status,update_time) " \
                           "VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    query_insert_station_weather = "INSERT INTO station_weather(id,station_id,lat,lng,weather_id,temp, feels_like," \
                                   " temp_min, temp_max, pressure, humidity, wind_speed, wind_deg, clouds, rain_1h," \
                                   " rain_3h, snow_1h, snow_3h, update_time, sid)" \
                                   "VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

    # Connect to the database
    server = depend_constant.DB_SERVER  # host name
    user = depend_constant.DB_USER  # user name
    password = depend_constant.DB_PASSWORD  # password

    # Create the instance of mysql.Mysql
    db = mysql.Mysql(server, 3306, user, password, "dbike")

    # Send the query and insert into table station
    db.executemany(query_insert_station, insert_data2station(depend_constant.API_KEY_JCD, "dublin"))

    # Select the sid of station to refresh station_weather
    sid_query = "select s.sid, s.lat, s.lng, s.station_id " \
                "from station s " \
                "left join station_weather sw on s.sid = sw.sid " \
                "where sw.sid is null"

    # Get the return data from db query
    sid_return = db.query(sid_query)
    station_weather_renew_row = 0
    for sid_dict in sid_return:
        # Get the parameter to generate table station_weather
        lat_wea = sid_dict['lat']
        lon_wea = sid_dict['lng']
        sid_wea = sid_dict['sid']
        station_id_wea = sid_dict['station_id']
        # Insert into station_weather table
        db.executemany(query_insert_station_weather,
                       insert_data2weather(lat_wea, lon_wea, sid_wea, station_id_wea, depend_constant.API_KEY_OW))
        # Count the number of refreshed rows
        station_weather_renew_row += 1

    # Count the number of rows
    station_renew_row = len(insert_data2station(depend_constant.API_KEY_JCD, "dublin"))
