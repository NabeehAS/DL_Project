import requests
import time
import random
import os
import progressbar
from cordinates import generate_random_coordinates
from cordinates import get_country_from_coordinates
 
# replace with your own google API key
API_KEY = 'get your own'
BASE_URL = 'https://maps.googleapis.com/maps/api/streetview'
META_URL = 'https://maps.googleapis.com/maps/api/streetview/metadata'
count = 0
radius = 20000

def get_image_in_radius(location):
    global count
    global radius
    params_meta = {
        'location': f'{location[0]},{location[1]}',
        'radius': radius,
        'source': 'outdoor',
        'key': API_KEY
    }
    meta =  requests.get(META_URL,params=params_meta)
    count+=1
    meta_data = meta.json()
    if meta.status_code != 200 or meta_data['status'] != 'OK' or meta_data['copyright'] != '© Google':
        return -1 
    return [meta_data['location']['lat'],meta_data['location']['lng']]

def get_street_view_image(location, image_num, country):
    global count
    temp = get_image_in_radius(location)
    if temp == -1:
        return -1
    location = temp
    if random.randint(1, 50) == 3:#random
        if get_country_from_coordinates(location[0],location[1]) != country:
            return -1
    heading = str(random.randint(0,359)) # Direction of camera (0 to 360)
    size = '256x256' # Image size
    fov = '90' # Field of view
    params = {
        'size': size,
        'location': f'{location[0]},{location[1]}',
        'heading': heading,
        'fov': fov,
        'pitch': '0',
        'key': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    count+=1
    if response.status_code != 200:
        print(response)
        return -1
    country_dir = 'D:\\AI_project\\dataset\\'+country
    image_path = os.path.join(country_dir, f'{country}_{image_num}.jpg')
    with open(image_path, 'wb') as file:
        file.write(response.content)
    return 0

# Collect images
#countries = ['US', 'JP', 'CA', 'MX', 'GT', 'PA', 'CO', 'EC', 'PE', 'BR',
#              'CL', 'UY', 'AR', 'IS', 'NO', 'SE', 'FI', 'UK', 'IE', 'DK', 'EE', 'LV', 'LT', 'PL', 
#             'DE', 'NL', 'BE', 'LU', 'FR', 'CH', 'ES', 'PT', 'CZ', 'AT', 'SK', 'SI', 'HU', 'HR', 
#              'IT', 'UA', 'RS', 'RO', 'BG', 'GR', 'TR', 'RU', 'CY', 'IL', 'LB', 'JO', 'QA', 'IN', 
#             'BD', 'PH', 'TW', 'KR', 'TH', 'KH', 'LK', 'MY', 'SG', 'ID', 'AU', 'NZ', 'KE', 'NG', 
#              'MN', 'SN', 'ZA', 'LS', 'SZ']

with open('D:\\AI_project\\alpha2.txt','r') as alpha2:
    
    country = alpha2.readline().strip()
    while country:
        count = 0
        os.makedirs('D:\\AI_project\\dataset\\'+country, exist_ok=True)
        print("collecting "+country)
        widgets = [progressbar.Bar('-'),' (',progressbar.ETA(), ') ',] #show progress
        bar = progressbar.ProgressBar(maxval=400,widgets=widgets).start() #show progress
        i = 1
        if country == 'US':
            i += 201
        while i < 401:
            coord = generate_random_coordinates(country)
            if coord == -1:
                time.sleep(2)
                continue
            result = get_street_view_image(coord,i+600,country)
            if result != 0:
                continue
            bar.update(i)
            i+=1
        bar.finish()    
        print("API calls for : "+country)
        print(count)
        country = alpha2.readline().strip()
