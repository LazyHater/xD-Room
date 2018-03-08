import requests
import constants
import json
from datetime import datetime

url = (constants.SUNSET_API['url'].format(**constants.SUNSET_API))
r = requests.get(url)
d = json.loads(r.content)
#print (r.content)
#print (d)
sunrise = d['results']['sunrise']
sunset = d['results']['sunset']
print (sunrise)
print (sunset)

def str_to_datetime(string):
    return datetime.strptime(string[:-6], "%Y-%m-%dT%H:%M:%S")

print (str_to_datetime(sunrise))
print (str_to_datetime(sunset))

def isDayNow(sunrise, sunset):
    sunrise = str_to_datetime(sunrise)
    sunset = str_to_datetime(sunset)
    now = datetime.now()
    if (now > sunrise) and (now < sunset):
        return True
    return False
    
print (isDayNow(sunrise, sunset))
