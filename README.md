# DeltaFleet 🚚

**DeltaFleet** is a multi-tenant fleet & logistics management SaaS platform designed to streamline operations for delivery, transportation, and logistics companies. It provides real-time visibility, role-based access control, and data-driven insights for managing drivers, vehicles, and delivery assignments — all in one place.

## 🚀 Key Features

- 🌐 **Multi-Tenant Architecture** — Each company has isolated data and admin access
- 🧑‍✈️ **Role-Based Dashboards** — Admins, Managers, and Drivers see only what they need
- 📍 **Real-Time Fleet Tracking** — Live trip monitoring with location updates
- 🗺️ **Smart Trip Management** — Assignments, routing, and delivery status updates
- 💼 **Billing & Reporting** — Subscription management and automated operational reports

## 🔐 User Roles

| Role     | Description                              |
|----------|------------------------------------------|
| Admin    | Full control over company fleet and users |
| Manager  | Assign trips and monitor drivers          |
| Driver   | View/update own delivery assignments      |

## 💡 Technologies

- **Backend:** Django, Django REST Framework, PostgreSQL, Celery
- **Frontend:** Vue.js with Vue Router & Pinia
- **Real-Time:** Django Channels + WebSocket
- **DevOps:** Docker, Redis, GitHub Actions, Prometheus/Grafana

## 🏁 Goal

Provide logistics teams a scalable, secure, and real-time SaaS platform to improve fleet efficiency, reduce operational friction, and deliver faster.


## 🚀 Tech Stack

### Backend:

* Django 4.x + Django Rest Framework
* PostgreSQL
* Celery + Redis
* JWT Authentication
* Multi-tenancy support (schema-based)
* Docker + Docker Compose

### Frontend:

* Vue.js 2 (Vue CLI)
* Vue Router, Vuex
* Axios for API

---

## ⚙️ Setup Instructions

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm install
cp .env.example .env
npm run serve
```

---

## 📦 Core Features

* Vehicle and Driver Management
* Real-time GPS Tracking
* Route Optimization (Google Maps or OpenRouteService)
* Role-based access control
* Subscription Billing (Stripe-ready)
* Admin & Tenant dashboards

---

## 🔐 Auth

* JWT-based auth (djangorestframework-simplejwt)
* Vue frontend stores token in Vuex/localStorage
* Refresh token strategy (secure)

---
