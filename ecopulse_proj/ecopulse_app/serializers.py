from rest_framework import serializers
from .models import ProjectSite, EnvironmentalMetric, Resource, Allocation, MetricType, ResourceCategory, UserProfile
from django.contrib.auth.models import User

class ProjectSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSite
        fields = '__all__'

class EnvironmentalMetricSerializer(serializers.ModelSerializer):        
    site_name = serializers.ReadOnlyField(source='project_site.name')
    metric_name = serializers.ReadOnlyField(source='metric_type.name')

    class Meta:
        model = EnvironmentalMetric
        fields = ['id', 'project_site', 'site_name', 'metric_type', 'metric_name', 'value', 'recorded_at']
        
class ResourceSerializer(serializers.ModelSerializer):        
    # This allows me to see the category name in the list
    category_name = serializers.ReadOnlyField(source='category.name')
    
    class Meta:
        model = Resource
        fields = ['id', 'name', 'category', 'category_name', 'status']

class AllocationSerializer(serializers.ModelSerializer):
    # This shows the actual names in the API instead of just ID numbers
    user_name = serializers.ReadOnlyField(source='user.username')
    resource_name = serializers.ReadOnlyField(source='resource.name')
    site_name = serializers.ReadOnlyField(source='site.name')

    class Meta:
        model = Allocation
        fields = [
            'id', 'user', 'user_name', 'resource', 'resource_name', 
            'site', 'site_name', 'checkout_date', 'return_date'
        ]

class MetricTypeSerializer(serializers.ModelSerializer):        
    class Meta:
        model = MetricType
        fields = '__all__'

class ResourceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceCategory
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):        
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'role', 'phone_number', 'assigned_region']

