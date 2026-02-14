import requests
from django.conf import settings
import polyline


def get_route(start_coords, end_coords):
    url = "https://api.openrouteservice.org/v2/directions/driving-car"

    headers = {
        "Authorization": settings.ORS_API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "coordinates": [
            [start_coords[1], start_coords[0]],  # ORS expects [lng, lat]
            [end_coords[1], end_coords[0]]
        ]
    }

    response = requests.post(url, json=body, headers=headers)
    data = response.json()

    route = data["routes"][0]

    encoded_geometry = route["geometry"]

    # 🔥 Decode polyline
    decoded_geometry = polyline.decode(encoded_geometry)

    # polyline gives (lat, lng) — convert to (lng, lat)
    decoded_geometry = [(lng, lat) for lat, lng in decoded_geometry]

    return {
        "geometry": decoded_geometry,
        "distance_meters": route["summary"]["distance"]
    }
