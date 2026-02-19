from django.shortcuts import render
from .serializers import ProjectSiteSerializer, ResourceSerializer, EnvironmentalMetricSerializer, AllocationSerializer, ResourceCategorySerializer, MetricTypeSerializer, UserProfileSerializer
from rest_framework import viewsets, permissions, status
from .models import ProjectSite, Resource, EnvironmentalMetric, Allocation, ResourceCategory, MetricType, UserProfile
from rest_framework.response import Response

# Create your views here.

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Admins can do anything. 
    Volunteers can only view (GET).
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_userprofile.role == 'Admin'

class ProjectSiteViewSet(viewsets.ModelViewSet):
    queryset = ProjectSite.objects.all()
    serializer_class = ProjectSiteSerializer
    permission_classes = [IsAdminOrReadOnly] #Admin manage sites, volunteers can only read

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAdminOrReadOnly]

class EnvironmentalMetricViewSet(viewsets.ModelViewSet):    
    queryset = EnvironmentalMetric.objects.all()
    serializer_class = EnvironmentalMetricSerializer
    # Volunteers NEED to be able to post data from the field
    permission_classes = [permissions.IsAuthenticated] # Both Admins and Volunteers can manage metrics, but must be logged in.

class AllocationViewSet(viewsets.ModelViewSet):    
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer
    permission_classes = [permissions.IsAuthenticated] # Both Admins and Volunteers can manage allocations, but must be logged in.
    
    def perform_create(self, serializer):
        # 1. Save the allocation
        allocation = serializer.save()
        # 2. Automatically flip the resource status to 'In Use'
        resource = allocation.resource
        resource.status = 'In Use'
        resource.save()

class ResourceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ResourceCategory.objects.all()
    serializer_class = ResourceCategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class MetricTypeViewSet(viewsets.ModelViewSet):
    queryset = MetricType.objects.all()
    serializer_class = MetricTypeSerializer
    permission_classes = [IsAdminOrReadOnly]

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAdminUser] # Only real Admins can edit roles.
