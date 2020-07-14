from django.urls import include, path
from rest_framework import routers
from .views import *

# --- api routes ---
router = routers.DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')
router.register(r'enrolled', EnrolledViewSet, basename='enrolled')
router.register(r'majors', MajorViewSet, basename='majors')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'subcategories', SubCategoryViewSet, basename='subcategories')
router.register(r'requirements', RequirementViewSet, basename='requirements')
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'prereqs', PrereqViewSet, basename='prereqs')
router.register(r'apcredits', ApCreditViewSet, basename='apcredits')


urlpatterns = [
    # automatic API URL routing.
    path('', include(router.urls)),
    # login URLs for the browsable API.
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # get operation for relations
    path("linkStudentAndEnrollment/<student_pk>/<enrollment_pk>/", linkStudentAndEnrollment),
    path("linkEnrollmentAndMajor/<enrollment_pk>/<major_pk>/", linkEnrollmentAndMajor),
    path("linkMajorAndCategory/<major_pk>/<category_pk>/", linkMajorAndCategory),
    path("linkCategoryAndSubcategory/<category_pk>/<subcategory_pk>/", linkCategoryAndSubcategory),
    path("linkSubcategoryAndRequirement/<subcategory_pk>/<requirement_pk>/", linkSubcategoryAndRequirement),
    path("linkRequirementAndCourse/<requirement_pk>/<course_pk>/", linkRequirementAndCourse),
    path("linkCourseAndPrereq/<course_pk>/<prereq_pk>/", linkCourseAndPrereq),
    path("linkCourseAndAp/<course_pk>/<ap_pk>/", linkCourseAndAp),
    path("majorlist/<username>/", requestMajorList),
    path("categorylist/<username>/<major_name>/", requestCategoriesList),
    path("subcategorylist/<username>/<major_name>/<category_name>/", requestSubcategoriesList),
    path("requirementlist/<username>/<major_name>/<category_name>/<subcategory_name>/", requestRequirementsList),
    path("courselist/<username>/<major_name>/<category_name>/<subcategory_name>/<requirement_name>/", requestCoursesList),
    path("prereqlist/<username>/<major_name>/<category_name>/<subcategory_name>/<requirement_name>/<course_name>/", requestPrereqList),
    path("aplist/<username>/<major_name>/<category_name>/<subcategory_name>/<requirement_name>/<course_name>/", requestApList),
    path("specificsubcategory/<username>/<major_name>/<category_name>/<subcategory_name>/", requestSubcategoryNote),
    path("specificrequirement/<username>/<major_name>/<category_name>/<subcategory_name>/<requirement_name>/", requestRequirementCredit),
    path("specificcourse/<username>/<major_name>/<category_name>/<subcategory_name>/<requirement_name>/<course_name>/", requestCoursesCredit),
]
