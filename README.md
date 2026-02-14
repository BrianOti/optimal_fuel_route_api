🚗 Route Fuel Optimization API

A Django REST API that calculates optimal fuel stops along a driving route within the United States.

The system:

Computes total driving distance using a routing API

Determines required fuel stops based on a 500-mile vehicle range

Selects cost-effective fuel stations along the route

Calculates total fuel cost assuming 10 MPG

Returns route geometry for map rendering

Minimizes external API calls for performance

📌 Features

Django (latest stable)

Django REST Framework

External routing API integration (single API call per request)

CSV fuel price ingestion into database

Geographic filtering using Haversine distance

Optimized geometry response (downsampled for performance)

Clean service-layer architecture

🧠 Assumptions

Vehicle maximum range: 500 miles

Fuel efficiency: 10 miles per gallon

Tank capacity: 50 gallons

Fuel prices are sourced from the provided CSV file

Routing is handled via a free routing API

🏗 Architecture
routeplanner/

── services/
   ── routing.py          # External routing API logic
   ── fuel_optimizer.py   # Fuel stop & cost calculations

── models.py               # FuelStation model
── views.py                # API endpoint logic

Separation of Concerns

routing.py → Fetches route distance & geometry

fuel_optimizer.py → Handles fuel stop optimization & cost calculation

views.py → Orchestrates request/response logic

This ensures clean, maintainable code.

⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/yourusername/route-fuel-api.git
cd route-fuel-api

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Environment Variables

Create a .env file in the project root:

ROUTING_API_KEY=your_api_key_here

5️⃣ Apply Migrations
python manage.py migrate

6️⃣ Load Fuel Price Data
python manage.py shell


Import CSV data into FuelStation model.

(Or use your custom management command if implemented.)

7️⃣ Run Server
python manage.py runserver

🚀 API Usage
Endpoint
POST /api/route/

Request Body
{
    "start": "Dallas, TX",
    "end": "Nashville, TN"
}

Response Example
{
    "distance_miles": 705.89,
    "fuel_stops": [
        {
            "name": "7-ELEVEN #218",
            "city": "Harrold",
            "state": "TX",
            "price": 2.68733333,
            "gallons_filled": 50.0
        }
    ],
    "total_fuel_cost": 189.7,
    "route_geometry": [...]
}

🧮 Fuel Cost Calculation
Total Gallons = Total Distance / MPG
Total Cost = Total Gallons × Fuel Price


Example:

705 miles

10 MPG

70.5 gallons required

Multiplied by selected station price

📍 Geographic Optimization

Fuel stations are filtered using:

Route geometry returned by routing API

Haversine distance formula

Configurable radius threshold

Geometry sampling to improve performance

This ensures:

Stations are near the route

Reduced computation overhead

Efficient response times

⚡ Performance Considerations

Routing API is called only once per request

Route geometry is downsampled before return

Fuel stations are filtered efficiently

Minimal database queries

Lightweight JSON responses

🔮 Possible Future Improvements

Segment-based fuel optimization (per 500-mile chunk)

Caching routing results

Real-time fuel price updates

Redis caching layer

Frontend map visualization

Docker containerization

🛠 Tech Stack

Python

Django

Django REST Framework

External Routing API

SQLite / PostgreSQL
