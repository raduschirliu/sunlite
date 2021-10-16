import requests
import os

token = os.getenv('LIFX_KEY')

headers = {
    "Authorization": "Bearer %s" % token,
}

def start_sunrise():
    # 2000k -> 4500k
    minutes = 1
    set_colour("2500")
    fade_colour(2000, 0.5, minutes*60)
    

def set_colour(kelvin):
    payload = { 
        "power": "on",
        "color": "kelvin:" + kelvin + " saturation:1",
        "brightness": 0,
        "duration": 0
    }

    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    print(response)


def fade_colour(delta_kelvin, delta_brightness, duration):
    payload = { 
        "power": "on",
        "duration": duration,
        "kelvin": delta_kelvin,
        "brightness": delta_brightness   
    }

    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    print(response)