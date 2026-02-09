Ride Sharing API (Django + DRF + WebSockets)

A backend Ride Sharing system built using Django, Django REST Framework, and Django Channels.
Supports rider & driver roles, JWT authentication, ride lifecycle management, driver matching, and real-time location tracking.

Features

Custom User model (Rider / Driver)

JWT Authentication (Login & Token Refresh)

Role-based permissions

Ride lifecycle management

Driver matching

Real-time location tracking using WebSockets

Swagger API documentation

Clean REST architecture

Tech Stack

Python 3.12

Django 6

Django REST Framework

Django Channels

Simple JWT

SQLite

Daphne (ASGI server)

Project Structure
ride_sharing_api/
├── users/
├── rides/
│   ├── consumers.py
│   ├── routing.py
│   └── utils.py
├── ride_sharing_api/
│   ├── settings.py
│   ├── asgi.py
│   └── urls.py
├── manage.py

Installation & Setup
1. Clone repository
git clone https://github.com/ranjithth73-tech/ride-sharing-api.git
cd ride-sharing-api

2. Create virtual environment
python -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py makemigrations
python manage.py migrate

5. Run server (REST APIs)
python manage.py runserver


Server:

http://127.0.0.1:8000


Swagger:

http://127.0.0.1:8000/swagger/

6. Run WebSocket server (Real-time)

Stop runserver and run:

daphne -p 8001 ride_sharing_api.asgi:application


WebSocket runs on:

ws://127.0.0.1:8001

Authentication Flow
Register
POST /api/auth/register

{
  "username": "user1",
  "password": "test123",
  "is_driver": false
}

Login
POST /api/auth/login


Use returned access token:

Authorization: Bearer <token>

Ride Flow
1. Create Ride (Rider)
POST /api/rides/

{
  "pickup_location": "MG Road",
  "dropoff_location": "Airport",
  "pickup_latitude": 12.9716,
  "pickup_longitude": 77.5946
}

2. Accept Ride (Driver)
POST /api/rides/{id}/accept/

3. Start Ride
POST /api/rides/{id}/start/

4. Complete Ride
POST /api/rides/{id}/completed/

Driver Matching
POST /api/rides/{id}/match_driver/


Matches nearest available driver using distance calculation.

Real-Time Location Tracking
Step 1: Connect WebSocket
ws://127.0.0.1:8001/ws/rides/{ride_id}/

Step 2: Update Location (Driver)
POST /api/rides/{ride_id}/update_location/

{
  "latitude": 12.99,
  "longitude": 77.55
}

Step 3: Receive Live Updates

WebSocket clients receive:

{
  "latitude": 12.99,
  "longitude": 77.55
}

Ride Status Flow
REQUESTED → ACCEPTED → STARTED → COMPLETED
       ↘ CANCELED

Notes

WebSockets work only with Daphne (ASGI)

Real-time updates are sent through Django Channels groups

Drivers can update location; riders receive live tracking

SQLite used for development

Author

Ranjith
