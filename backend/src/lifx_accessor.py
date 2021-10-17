import requests

def start_sunrise(api_token):
    headers = {
        "Authorization": "Bearer %s" % api_token,
    }

    # 2000k -> 4500k
    minutes = 5
    set_colour("1500", 0.0, 0.0, headers)
    set_colour("4500", 0.6, minutes*60.0, headers)
    
def disco():
    for i in range(10):
        set_colour("2000", 1.0, 0.03)
        set_colour("3000", 1.0, 0.03)
        set_colour("4000", 1.0, 0.03)
        set_colour("5000", 1.0, 0.03)


def set_colour(kelvin, brightness, duration, headers):
    payload = { 
        "power": "on",
        "color": "kelvin:" + kelvin + " saturation:1",
        "brightness": brightness,
        "duration": duration
    }

    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    print(response)

def set_colour_off(kelvin, headers):
    payload = { 
        "power": "on",
        "color": "kelvin:" + kelvin + " saturation:1",
        "brightness": 0,
        "duration": 0
    }

    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    print(response)


def fade_colour(delta_kelvin, delta_brightness, duration, headers):
    payload = { 
        "power": "on",
        "duration": duration,
        "kelvin": delta_kelvin,
        "brightness": delta_brightness   
    }

    response = requests.post('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    print(response)