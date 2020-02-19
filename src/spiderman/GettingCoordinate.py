import requests
import json

# Get location data of stations from JCDecaux
API_KEY_JCD = "bf6a214054531bd85d0445e047e084bb3d1c0975"
CONTRACT_JCD = "dublin"
jcd_response = requests.get(
    "https://api.jcdecaux.com/vls/v1/stations?contract=" + CONTRACT_JCD + "&apiKey=" + API_KEY_JCD)
print(jcd_response.json())

# Create a list to contain the result
result = []

# Get the number and coordinate from the api json file
for dict in jcd_response.json():
    temp_dict = {'number': dict['number'], 'lat': dict['position']['lat'], 'lon': dict['position']['lng']}
    result.append(temp_dict)

# Generate the local json only with number and coordinate by converting the list into a json file
with open('JCD_Coordinate.json', "w") as json_file:
    json.dump(result, json_file)
