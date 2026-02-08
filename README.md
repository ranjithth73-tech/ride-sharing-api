# 🚕 Ride Sharing API (Django + DRF)

This project is a **Ride Sharing Backend API** built using **Django Rest Framework (DRF)**. It supports **user and driver roles**, **JWT authentication**, **ride lifecycle management**, **driver matching**, and **simulated real-time tracking**.

This repository is suitable for **machine tasks**, **portfolio projects**, and **backend interviews**.

---

## 📌 Features

* User & Driver registration
* JWT-based authentication
* Role-based permissions (Rider vs Driver)
* Ride creation & lifecycle
* Driver matching using distance
* Simulated real-time ride tracking
* Clean REST APIs

---

## 🧱 Tech Stack

* Python 3.12
* Django 6.x
* Django REST Framework
* Simple JWT
* SQLite (development)

---

## 📂 Project Structure

```
ride_sharing_api/
├── users/        # Custom user model & auth
├── rides/        # Ride logic & APIs
├── utils.py      # Distance calculation
├── settings.py
├── urls.py
└── manage.py
```

---

## 🔐 Authentication Flow

* All users register & login using the same system
* JWT tokens are issued on login
* Role (`is_driver`) controls access to APIs

---

## 🚀 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <repo-url>
cd ride_sharing_api
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Start server

```bash
python manage.py runserver
```

Server runs at:

```
http://127.0.0.1:8000
```

---

## 🧪 API Usage (Step-by-Step)

### 1️⃣ Register User

```
POST /api/auth/register
```

```json
{
  "username": "rider1",
  "password": "test1234",
  "is_driver": false
}
```

---

### 2️⃣ Login User

```
POST /api/auth/login
```

```json
{
  "username": "rider1",
  "password": "test1234"
}
```

Copy the **access token** and use it as **Bearer Token**.

---

### 3️⃣ Create Ride (Rider)

```
POST /api/rides/
```

```json
{
  "pickup_location": "MG Road",
  "dropoff_location": "Airport",
  "pickup_latitude": 12.9716,
  "pickup_longitude": 77.5946
}
```

---

### 4️⃣ Accept Ride (Driver)

```
POST /api/rides/{id}/accept/
```

---

### 5️⃣ Start Ride

```
POST /api/rides/{id}/start/
```

---

### 6️⃣ Update Location

```
POST /api/rides/{id}/update_location/
```

```json
{
  "latitude": 12.975,
  "longitude": 77.599
}
```

---

### 7️⃣ Complete Ride

```
POST /api/rides/{id}/completed/
```

---

## 🎯 Driver Matching (Bonus)

```
POST /api/rides/{id}/match_driver/
```

* Matches nearest available driver
* Uses Haversine distance formula

---

## ✅ Status Flow

```
REQUESTED → ACCEPTED → STARTED → COMPLETED
       ↘ CANCELED
```

---

## 🧠 Notes

* Real-time tracking is simulated using polling
* Architecture is WebSocket-ready
* Clean separation of concerns

---

## 📌 Author

Ranjith

---

## ⭐ If you like this project

Give it a ⭐ on GitHub
