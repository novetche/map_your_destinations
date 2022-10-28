# LOCATIONS TO VISIT BEFORE DEATH, ON THE MAP OF YOUR CHOICE

## INFORMATIONS

#### Description
This program written in Python allows the user to display on a map the places he want to visit in his life as well as the ones he has already visited, so that he don't forget anything and can recall memories.
The program connects to Notion, a notes and database software, via a REST API to import data from a Notion table containing the name of the place, its city, its country as well as a checkbox indicating if he has been there or not.
Then, after processing the imported data, the program adds geolocation information, latitude and longitude for each location, allowing it to create markers on a map.
Finally, the program opens a map in the user's browser, which will have the style selected by the user when opening the program including styles such as black&white, 3D or Darth Vader.
The user can of course continue to add new destinations and update the map as he/she travels.

#### My development journey
To develop this program, I have researched Notion API and how to create map with Python.
The plan was:
- the V1 will allow to see the locations I want to visit before I die
- the V2 will allow to tick the places visited, and change the marker color on map, and thus improve the user experience
- the V3 will allow to make it possible for the user to select the map style
- the V4 could allow recommendations to be made to the user based on their visited places
- V5 to add images
etc.

I have developed this program to the V3 stage for the final test of the course CS50 Python from Harvard University and I hope you will like it.

### User story
As the user, I want to see on a map the different places I want to visit in my life so that I can remember them, project myself and show them to my friends & family

### Acceptance criteria
- Given a database on Notion filled with locations the user wants to visit during his life, or have already visited, with name of location, name of city, country, and the status of the visit,
- When the user run this Python program "map_from_database.py", he will select the map style,
- Then through a connection to Notion, Python will display a map with all the places the user wants to visit or have visited.

### Unit Tests
- on file "test_mainfile.py"

## TECHNICAL INFORMATIONS
### APIs
- Notion API REST
    - Internal Integration Token = "your_integration_token"
    - Database ID = "your_database_id"
### Libraries
- requests
- json
- geopy
- plotly.express
