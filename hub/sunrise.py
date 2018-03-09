import requests
import json
from datetime import datetime


def get_sunrise_and_sunset(url):
    r = requests.get(url)
    d = json.loads(r.content)
    sunrise = d['results']['sunrise']
    sunset = d['results']['sunset']
    return sunrise, sunset

def str_to_datetime(string):
    return datetime.strptime(string[:-6], "%Y-%m-%dT%H:%M:%S")

def is_day_now(sunrise, sunset):
    sunrise = str_to_datetime(sunrise)
    sunset = str_to_datetime(sunset)
    now = datetime.utcnow()
    if (now > sunrise) and (now < sunset):
        return True
    return False
    
if __name__ == "__main__":
    from constants import SUNRISE_URL as url
    print (is_day_now(*get_sunrise_and_sunset(url)))
