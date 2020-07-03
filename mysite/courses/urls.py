from django.urls import include, path
from rest_framework import routers
from . import views

# --- api routes ---
router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet, basename='students')
router.register(r'enrolled', views.EnrolledViewSet, basename='enrolled')
router.register(r'majors', views.MajorViewSet, basename='majors')
router.register(r'categories', views.CategoryViewSet, basename='categories')
router.register(r'subcategories', views.SubCategoryViewSet, basename='subcategories')
router.register(r'requirements', views.RequirementViewSet, basename='requirements')
router.register(r'courses', views.CourseViewSet, basename='courses')
router.register(r'prereqs', views.PrereqViewSet, basename='prereqs')
router.register(r'apcredits', views.ApCreditViewSet, basename='apcredits')

urlpatterns = [
    # automatic API URL routing.
    path('', include(router.urls)),
    # login URLs for the browsable API.
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   
]
