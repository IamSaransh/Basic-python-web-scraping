import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=28.56604489500006&lon=-81.68864878999995#.XrArYWgza00')
soup = BeautifulSoup(page.content,'html.parser')
week = soup.find(id = 'seven-day-forecast-body')
#print(week)
items = week.find_all(class_='tombstone-container')


period_names = [item.find(class_='period-name').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]


# some other way
# period_names = []  

# for item in items:
#     period_names.append(item.find(class_='period-name').get_text()) 
#    print(period_names)
weather_stuff = pd.DataFrame(
    { 'period' : period_names,
      'short_description' : short_description,
      'temperaturess' : temperatures,
    }
)
print(weather_stuff)
#also to save it as a csv file
weather_stuff.to_csv('weather.csv')

   


