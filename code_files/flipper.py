import os
from PIL import Image

image_folder = ".\\dataset"
sub =  ['AR', 'AT', 'BE', 'BR', 'CA', 'CH', 'CL', 'CZ', 'DE', 'DK', 'EE', 'ES', 'FI', 'FR', 'IE', 'IL', 'IN', 'JP', 'KR', 'MX', 'NL', 'NO', 'NZ', 'PL', 'PT', 'SE', 'TH', 'UK', 'US', 'ZA']

for name in sub:
    working = image_folder+'\\'+name
    for filename in os.listdir(working):
        file_path = os.path.join(working, filename)
        if filename.endswith('f.jpg'):
            os.remove(file_path)
        
