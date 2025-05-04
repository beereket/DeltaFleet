# DeltaFleet

DeltaFleet is a multi-tenant fleet and logistics SaaS platform built with Django, PostgreSQL, and Vue 2, featuring real-time tracking, optimized routing, and modular architecture suitable for cloud deployment.

---

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
