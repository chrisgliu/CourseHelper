# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'majors', views.MajorViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'subcategories', views.SubCategoryViewSet)
router.register(r'requirements', views.RequirementViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'prereqs', views.PrereqViewSet)
router.register(r'apcredits', views.ApCreditViewSet)

# using automatic API URL routing.
# login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
