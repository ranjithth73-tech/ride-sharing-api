# Ride Sharing API

A backend API for a ride-sharing system built using **Django**, **Django REST Framework**, and **Django Channels**.  
Supports **Rider and Driver roles**, **JWT authentication**, **ride lifecycle management**, **driver matching**, and **real-time location tracking via WebSockets**.

---

## Tech Stack
- Python 3.12
- Django 6.x
- Django REST Framework
- Django Channels (WebSockets)
- Simple JWT
- drf-yasg (Swagger)
- SQLite (Development)

---

## Features
- Custom User model (Rider / Driver)
- JWT Authentication
- Role-based access control
- Ride lifecycle:


REQUESTED → ACCEPTED → STARTED → COMPLETED
↘ CANCELED



- Driver matching using Haversine distance
- Real-time driver location updates
- Swagger API documentation
- Django Admin panel

---

## Setup

```bash
git clone https://github.com/ranjithth73-tech/ride-sharing-api.git
cd ride_sharing_api

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Server: http://127.0.0.1:8000

Swagger: http://127.0.0.1:8000/swagger/

Admin: http://127.0.0.1:8000/admin/



Authentication

Register

POST /api/auth/register/


Login

POST /api/auth/login/


Use the access token:

Authorization: Bearer <access_token>

Main APIs

Create Ride (Rider)

POST /api/rides/


Accept Ride (Driver)

POST /api/rides/{id}/accept/


Start Ride

POST /api/rides/{id}/start/


Update Driver Location

POST /api/rides/{id}/update_location/


Complete Ride

POST /api/rides/{id}/completed/


Cancel Ride

POST /api/rides/{id}/canceled/


Match Nearest Driver

POST /api/rides/{id}/match_driver/

Real-Time Tracking

WebSocket endpoint:

ws://127.0.0.1:8000/ws/rides/<ride_id>/


Driver location updates are broadcast to connected clients in real time.

Author

Ranjith

Highlights

Clean REST architecture

Role-based permissions

Real-time tracking using Django Channels

Swagger documentation




---
