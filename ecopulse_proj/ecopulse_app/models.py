from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    # This links the resource to a specific ResourceCategory, 
    category = models.ForeignKey('ResourceCategory', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, default='Available') # e.g., Available, Checked Out

    def __str__(self):
        return self.name

class EnvironmentalMetric(models.Model):
    project_site = models.ForeignKey(ProjectSite, on_delete=models.CASCADE)
    metric_type = models.ForeignKey('MetricType', on_delete=models.PROTECT)
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
    
class ResourceCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name    
    
class MetricType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name    
    
class UserProfile(models.Model):
    # This links the profile to a unique User instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #This Defines the roles for "Staff vs. Volunteers" feature
    ROLE_CHOICES = [
        ('ADMIN', 'Admin/Staff'),
        ('VOLUNTEER', 'Volunteer'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='VOLUNTEER')
    phone_number = models.CharField(max_length=15, blank=True)
    assigned_region = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"    
    
# Signal to automatically create or update UserProfile when a User is created or updated
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        UserProfile.objects.get_or_create(user=instance)
        instance.userprofile.save()   

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()