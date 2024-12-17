import requests
import time
import random
import os
import progressbar
import xml.etree.ElementTree as ET
from geopy.geocoders import Nominatim

def generate_random_coordinates(country):
    #gets a countries initials (like IL for israel) and get a coordinate from the country
    address = "https://api.3geonames.org/randomland."
    address = address + country +'.json'
    response = requests.get(address)
    if response.status_code == 200:
        try:#response.json sometimes dosent work
            data = response.json()
            x,y = data['nearest']['latt'] , data['nearest']['longt']
            return (x,y)
        except:
            return -1
    else:
        time.sleep(2)
        return -1
    

def get_country_from_coordinates(lat, lon):
    geolocator = Nominatim(user_agent="make_sure_coord_in_country")
    try:
        location = geolocator.reverse((lat, lon), language="en")
        
        if location and 'country' in location.raw['address']:
            ret = location.raw['address'].get('country_code', None).upper()
            if ret == 'GB':
                return 'UK'
            return ret
        else:
            return "Country not found"
    except:
        return -1
    
num_coords = 1000 #int(input("how much?"))

print("Getting coordinates...")
with open('D:\\AI_project\\alpha2.txt','r') as alpha2:
    
    current_country = alpha2.readline()
    while current_country:
        current_country = current_country.rstrip()
        i = 1000
        count = 0
        cur = "D:\\AI_project\\coords\\"+current_country+"_coords.txt"
        if os.path.exists(cur):
            current_country = alpha2.readline()
            continue
        print("new country: "+current_country)
        widgets = [progressbar.Bar('*'),' (',progressbar.ETA(), ') ',] #show progress
        bar = progressbar.ProgressBar(maxval=num_coords,widgets=widgets).start() #show progress
        with open(cur,'w') as file:
            while i < num_coords:
                try:
                    coords = generate_random_coordinates(current_country)
                    if coords == -1:
                        continue
                    #if get_street_view_image(coords, 0, current_country) == -1:
                     #  continue
                    bar.update(i)
                    i+=1
                    to_save = str(coords[0])+","+str(coords[1])
                    file.write(str(to_save)+"\n")
                except:
                    continue
            bar.finish()
            #print("API calls for :"+current_country)
            #print(count)
        current_country = alpha2.readline()


