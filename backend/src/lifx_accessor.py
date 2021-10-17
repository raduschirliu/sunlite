import requests
import os

token = os.getenv('LIFX_KEY')

headers = {
    "Authorization": "Bearer %s" % token,
}

def start_sunrise():
    # 2000k -> 4500k
    minutes = 10
    set_colour("1500", 0.0, 0.0)
    set_colour("4500", 0.6, minutes*60.0)
    
def disco():
    for i in range(10):
        set_colour("2000", 1.0, 0.1)
        set_colour("3000", 1.0, 0.1)
        set_colour("4000", 1.0, 0.1)
        set_colour("5000", 1.0, 0.1)


def set_colour(kelvin, brightness, duration):
    payload = { 
        "power": "on",
        "color": "kelvin:" + kelvin + " saturation:1",
        "brightness": brightness,
        "duration": duration
    }

    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    print(response)

def set_colour_off(kelvin):
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

    response = requests.post('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    print(response)