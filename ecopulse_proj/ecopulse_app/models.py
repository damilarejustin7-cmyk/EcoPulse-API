from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
# Model for Project sites 
class ProjectSite(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    historical_context = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Available') # e.g., Available, Checked Out

    def __str__(self):
        return self.name

class EnvironmentalMetric(models.Model):
    project_site = models.ForeignKey(ProjectSite, on_delete=models.CASCADE)
    metric_type = models.CharField(max_length=100) # e.g., Carbon Level, Soil pH
    value = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)     

class Allocation(models.Model):
    # Link to the person (User), not the site
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Link to the actual Resource model so we can access .name
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    
    # Link to the ProjectSite
    site = models.ForeignKey(ProjectSite, on_delete=models.CASCADE)
    
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

# Use self.user.username and self.site.name to match fields
    def __str__(self):
        return f"{self.metric_type} at {self.project_site.name} ({self.value})"