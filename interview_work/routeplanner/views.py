from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .services.routing import get_route
from .services.geocoding import geocode
from .services.fuel_optimizer import calculate_fuel_plan

class RouteAPIView(APIView):

    def post(self, request):
        start = request.data.get("start")
        finish = request.data.get("finish")

        start_coords = geocode(start)
        finish_coords = geocode(finish)

        route_data = get_route(start_coords, finish_coords)

        miles = route_data["distance_meters"] * 0.000621371
        

        stops, total_cost = calculate_fuel_plan(miles)

        return Response({
            "distance_miles": round(miles, 2),
            "fuel_stops": stops,
            "total_fuel_cost": total_cost,
            "route_geometry": route_data["geometry"][::500]
        })
