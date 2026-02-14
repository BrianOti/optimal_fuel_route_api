import requests
from django.conf import settings

def geocode(location):
    url = "https://api.openrouteservice.org/geocode/search"

    params = {
        "api_key": settings.ORS_API_KEY,
        "text": location
    }

    response = requests.get(url, params=params)
    data = response.json()

    coords = data["features"][0]["geometry"]["coordinates"]

    return coords[1], coords[0]  # lat, lng