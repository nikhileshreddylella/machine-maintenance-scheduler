# Machine Maintenance Scheduler (Microservices)

## Overview
This project implements a Machine Maintenance Scheduling System for manufacturing plants using Microservices Architecture.

## Features
- Machine status management
- Maintenance scheduling
- Update maintenance records
- Inter-service communication
- Persistent database storage
- REST API implementation

## Architecture
Microservices-based system:
1. Machine Service (Port 8000)
2. Maintenance Service (Port 8001)

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Swagger API Documentation
- GitHub Version Control

## How to Run

Install dependencies:
pip install fastapi uvicorn sqlalchemy requests

Run services:

Machine Service:
uvicorn machine_service:app --port 8000

Maintenance Service:
uvicorn maintenance_service:app --port 8001

Open API Docs:
http://127.0.0.1:8000/docs
http://127.0.0.1:8001/docs# machine-maintenance-scheduler
