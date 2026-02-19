import os
import sys
import django

# This tells Python to look in the current folder for the ecopulse_proj folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 1. Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecopulse_proj.settings')
django.setup()

from ecopulse_app.models import ProjectSite, Resource, ResourceCategory

def seed_db():
    print("Seeding database...")

    # Create Categories
    cat_tools, _ = ResourceCategory.objects.get_or_create(name="Field Tools")
    cat_sensors, _ = ResourceCategory.objects.get_or_create(name="Electronic Sensors")

    # Create Project Sites
    sites = [
        {"name": "Kano Reforestation Zone", "location": "Kano, Nigeria"},
        {"name": "Lagos Coastal Watch", "location": "Lekki, Lagos"},
        {"name": "Ibadan Soil Health", "location": "Oyo State"}
    ]

    for site_data in sites:
        site, created = ProjectSite.objects.get_or_create(**site_data)
        if created:
            print(f"Created Site: {site.name}")

    # Create Resources (Equipment)
    resources = [
        {"name": "Soil PH Meter", "category": cat_sensors, "status": "Available"},
        {"name": "Standard Shovel", "category": cat_tools, "status": "Available"},
        {"name": "Drone Mapper v2", "category": cat_sensors, "status": "In Use"},
    ]

    for res_data in resources:
        res, created = Resource.objects.get_or_create(**res_data)
        if created:
            print(f"Created Resource: {res.name}")

    print("Seeding complete! Your app is now full of data.")

if __name__ == "__main__":
    seed_db()