from django.shortcuts import render
from .serializers import ProjectSiteSerializer, ResourceSerializer, EnvironmentalMetricSerializer, AllocationSerializer, ResourceCategorySerializer, MetricTypeSerializer, UserProfileSerializer
from rest_framework import viewsets
from .models import ProjectSite, Resource, EnvironmentalMetric, Allocation, ResourceCategory, MetricType, UserProfile

# Create your views here.
class ProjectSiteViewSet(viewsets.ModelViewSet):
    queryset = ProjectSite.objects.all()
    serializer_class = ProjectSiteSerializer

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class EnvironmentalMetricViewSet(viewsets.ModelViewSet):    
    queryset = EnvironmentalMetric.objects.all()
    serializer_class = EnvironmentalMetricSerializer

class AllocationViewSet(viewsets.ModelViewSet):    
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer


class ResourceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ResourceCategory.objects.all()
    serializer_class = ResourceCategorySerializer

class MetricTypeViewSet(viewsets.ModelViewSet):
    queryset = MetricType.objects.all()
    serializer_class = MetricTypeSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    