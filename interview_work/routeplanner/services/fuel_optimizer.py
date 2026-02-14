from routeplanner.models import FuelStation
import math

MAX_RANGE = 500
MPG = 10
TANK_CAPACITY = MAX_RANGE / MPG  # 50 gallons


def calculate_fuel_plan(total_miles):

    # Get cheapest fuel station (cost optimization)
    cheapest_station = FuelStation.objects.order_by("retail_price").first()

    if not cheapest_station:
        return [], 0

    selected_stops = []
    total_cost = 0

    miles_remaining = total_miles
    fuel_in_tank = TANK_CAPACITY  # start full tank

    while miles_remaining > 0:

        max_miles_with_current_fuel = fuel_in_tank * MPG

        if max_miles_with_current_fuel >= miles_remaining:
            # Final stretch
            gallons_used = miles_remaining / MPG
            total_cost += gallons_used * cheapest_station.retail_price
            miles_remaining = 0

        else:
            # Drive until tank empty
            miles_remaining -= max_miles_with_current_fuel

            gallons_filled = TANK_CAPACITY
            total_cost += gallons_filled * cheapest_station.retail_price

            selected_stops.append({
                "name": cheapest_station.name,
                "city": cheapest_station.city,
                "state": cheapest_station.state,
                "price": cheapest_station.retail_price,
                "gallons_filled": gallons_filled
            })

            fuel_in_tank = TANK_CAPACITY

    return selected_stops, round(total_cost, 2)
