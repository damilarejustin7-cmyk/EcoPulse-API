# EcoPulse-API
Its for  an Eco-Impact NGO Tracker 
Eco-Impact NGO Tracker API Overview: Eco-Pulse API is a specialized backend solution for environmental NGOs in Nigeria, tracking restoration projects (e.g., reforestation in Kano, soil recovery in Delta), logging climate metrics, and managing field equipment.

Key Features
Project Site Management

Full CRUD: Create, view, update, and archive sites.

Categorization: By type (e.g., Reforestation, Soil Recovery) and geographic location.

Climate Metric Logging

Field Data: Real-time metrics like tree counts, carbon levels, soil pH.

Accountability: Logs linked to specific sites and staff members.

Resource Allocation (Equipment Tracking)

Checkout System: Assign tools (sensors, shovels, seedlings) to sites.

Inventory Logic: Prevents double-booking and tracks availability.

Security & Roles
Access Control: Admins manage sites/resources; Volunteers log data.

JWT Authentication: Secure token-based access for field mobile use.

Tech Stack
Framework: Django 5.x

API Toolkit: Django REST Framework (DRF)

Database: MySQL / PostgreSQL (via Django ORM)

Auth: JWT (JSON Web Tokens)

Deployment: PythonAnywhere / Heroku

API Endpoints (Quick Reference)
GET /api/projects/: List all active project sites (Public/Auth).

POST /api/projects/: Create a new project site (Admin Only).

GET /api/projects/{id}/metrics/: View climate data for a site (Auth).

POST /api/resources/: Assign a tool/resource to a site (Admin/Staff).

DELETE /api/resources/{id}/: Mark a tool as returned (Admin/Staff).

Database Schema
Five core models for data integrity:

User: Staff and Volunteers.

ProjectSite: Locations and site details.

EnvironmentalMetric: Climate data logs.

Resource: Inventory of tools and equipment.

Allocation: Transaction log for borrowed resources.
