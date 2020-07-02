from django.urls import include, path
from rest_framework import routers
from . import views

# --- api routes ---
router = routers.DefaultRouter()
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
    # courses requests
    path('requestmajors/', views.requestMajors, name='request_majors'),
    path('requestcategories/<major_name>/', views.requestCategories, name='request_categories'),
    path('requestsubcategories/<category_name>/', views.requestSubCategories, name='request_subcategories'),
    path('requestrequirements/<subcategory_name>/', views.requestRequirements, name='request_requirements'),
    path('requestcourses/<requirement_name>/', views.requestCourses, name='request_courses'),
    path('requestprereqs/<course_name>/', views.requestPrereqs, name='request_prereqs'),
    path('requestap/<course_name>/', views.requestAP, name='request_ap'),
]
