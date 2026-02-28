from django.contrib import admin
from .models import UserProfile, ProjectSite, Resource, EnvironmentalMetric, Allocation, ResourceCategory, MetricType

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ProjectSite)
admin.site.register(Resource)
admin.site.register(EnvironmentalMetric)
admin.site.register(Allocation)
admin.site.register(ResourceCategory)
admin.site.register(MetricType)
