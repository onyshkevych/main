""" map """
import folium
import math
from geopy.geocoders import Nominatim
def locations(path: str, year:int, latitude: float, longitude: float):
    """
    This function creates a 
    """
    with open(path, 'rb') as list:
        lines = list.readlines()
        for line in lines:
            line = line.strip()
            if line[0] == "'":
                for element in line:
                    if element == '{':
                        start = line.index(element)
                    if element == '}':
                        final = line.index(element)
                    line = line[:start] + line[final + 1:]        
                    years = ""
                    if element.isdigit():
                        years += element
                cities = []
                year = int(input())
                latitude = float(input())
                longitude = float(input())
                if int(years) == year:
                    ind = line.index(year[-1] + 2)
                    cities.append(line[ind:])
                    years = ""
                for city in cities:   
                    geolocator = Nominatim(user_agent="location")
                    location = geolocator.geocode(city)
                    R = 6371e3
                    f_1 = latitude * math.pi/180
                    f_2 = location.latitude * math.pi/180
                    ff = (location.latitude - latitude) * math.pi/180
                    ll = (location.longitude - longitude) * math.pi/180
                    aa = (math.sin(ff/2) ** 2) + (math.cos(f_1) * math.cos(f_2)) * math.sin(ll/2) ** 2
                    cc = 2 * math.atan2(math.sqrt(aa), math.sqrt(1-aa))
                    distance = R * cc
                    cities.append(distance)
                distances = []
                mista = []
                mitkas = []
                for i in cities:
                    loc = cities.index(i)
                    if loc % 2 != 0:
                        distances.append(i)
                    else:
                        mista.append(i)
                    for j in distances:
                        if j == min(distances):
                            dic = distances.index(j)
                            mitkas.append(mista[dic])
                            for mitka in mitkas:
                                locatia = geolocator.geocode(mitka)
                                mitkas.append(locatia.latitude)
                                mitkas.append(locatia.longitude)
                return mitkas
def maping(path: str, year:int, latitude: float, longitude: float):
    data = locations(path, year, latitude, longitude)
    map = folium.Map(location=[data[1], data[2]],
    zoom_start=10)
    fg = folium.FeatureGroup(name = data[0])
    fg.add_child(folium.Marker(location =[data[1], data[2]],
                icon=folium.Icon(color = "yellow")))
    map.add_child(fg)
    map.add_child(folium.LayerControl())
    map.save('Map_Custom_Popup.html')