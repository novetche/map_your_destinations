import json
import requests
from geopy.geocoders import Nominatim
import plotly.express as px

def main():
    user_input = input(str(
        f"Hi you! Please choose your map style:\n 1) Basic Map AKA open-street-map\n 2) Grey&White AKA carto-positron\n 3) Darth Vader map AKA carto-darkmatter\n 4) Relief 3D map AKA stamen-terrain\n 5) Black&White AKA stamen-toner\n 6) Azure & Sand map (very beautiful) AKA stamen-watercolor\n Enter your choice number [1/2/3/4/5/6] here: "))
    while user_input not in ["1","2","3","4","5","6"]:
        print(f"\nNot a number between 1 and 6!\n")
        user_input = input(str(
        f"Please choose your map style:\n 1) Basic Map AKA open-street-map\n 2) Grey&White AKA carto-positron\n 3) Darth Vader map AKA carto-darkmatter\n 4) Relief 3D map AKA stamen-terrain\n 5) Black&White AKA stamen-toner\n 6) Azure & Sand map (very beautiful) AKA stamen-watercolor\n Enter your choice number [1/2/3/4/5/6] here: "))
    mapstylebrut = get_mapstyle_from_user(user_input)
    mapstyle = str(mapstylebrut)
    print("Wait for the map to appear..")
    locations = get_locations_names()
    n = 0
    lenloc = len(locations)
    while n < lenloc:
        cityname = locations[n]["city"]
        lat, lon = get_city_geodata(cityname)
        locations[n]["lat"]=float(lat)
        locations[n]["lon"]=float(lon)
        if locations[n]["visited"] is True:
            locations[n]["color"] = 1
        else:
            locations[n]["color"] = 0
        n += 1
    print_locations_on_map(locations, mapstyle)

def get_mapstyle_from_user(user_input):
    if user_input == "1":
        print("You choose Basic Map AKA open-street-map")
        mapstylebrut = "open-street-map"
    elif user_input == "2":
        print("You choose Grey&White AKA carto-positron")
        mapstylebrut = "carto-positron"
    elif user_input == "3":
        print("You choose Darth Vader map AKA carto-darkmatter")
        mapstylebrut = "carto-darkmatter"
    elif user_input == "4":
        print("You choose the relief 3D map AKA stamen-terrain")
        mapstylebrut = "stamen-terrain"
    elif user_input == "5":
        print("You choose Black&White AKA stamen-toner")
        mapstylebrut = "stamen-toner"
    elif user_input == "6":
        print("You choose Azure & Sand map (very beautiful) AKA stamen-watercolor")
        mapstylebrut = "stamen-watercolor"
    return mapstylebrut


def get_locations_names(
    database_id="YOUR DATABASE ID",
    integration_token="YOUR INTEGRATION TOKEN"
    ):
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    r = requests.post(url, headers={
    "Authorization": f"Bearer {integration_token}",
    "Notion-Version": "2022-06-28"
    })
    if r.status_code != 200:
        raise Exception(f'API Error, Response Status: {r.status_code}')
    else:
        result_dict = r.json()
        locations_list_result = result_dict["results"]
        locations = []
        for location in locations_list_result:
            locations_dict = ConvertResultToLocation(location)
            locations.append(locations_dict)
    return locations

def ConvertResultToLocation(result):
    properties = result["properties"]
    location = properties["location"]["title"][0]["text"]["content"]
    city = properties["city"]["rich_text"][0]["text"]["content"]
    country = properties["country"]["rich_text"][0]["text"]["content"]
    visited = properties["visited"]["checkbox"]
    return {
    "city": city,
    "location": location,
    "country": country,
    "visited": visited
    }

def get_city_geodata(cityname):
    geolocator = Nominatim(user_agent="MathisForCS50")
    geolocation = geolocator.geocode(cityname)
    lat = geolocation.latitude
    lon = geolocation.longitude
    return lat, lon

def print_locations_on_map(locations, mapstyle):
    fig = px.scatter_mapbox(
        locations, lat="lat", lon="lon", hover_name="location",
        hover_data=["city", "country", "visited"],
        color="color",
        color_continuous_scale=[(0, "red"),(1, "blue")],
        zoom=2, height=1000
    )
    fig.update_layout(mapbox_style=mapstyle)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

if __name__ == "__main__":
    main()