from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectSiteViewSet, ResourceViewSet, EnvironmentalMetricViewSet, AllocationViewSet, ResourceCategoryViewSet, MetricTypeViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'project-sites', ProjectSiteViewSet)
router.register(r'resources', ResourceViewSet)
router.register(r'environmental-metrics', EnvironmentalMetricViewSet)
router.register(r'allocations', AllocationViewSet)
router.register(r'resource-categories', ResourceCategoryViewSet)
router.register(r'metric-types', MetricTypeViewSet)
router.register(r'user-profiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]