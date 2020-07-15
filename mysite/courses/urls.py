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
    # get json list data
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
    # form operation create/delete
    path("createstudent", createListStudent),
    path("deletestudent", deleteListStudent),
    path("createenrollkey", createListEnroll),
    path("deleteenrollkey", deleteListEnroll),
    path("createmajor", createListMajor),
    path("deletemajor", deleteListMajor),
    path("createcategory", createListCategory),
    path("deletecategory", deleteListCategory),
    path("createsubcategory", createListSubCategory),
    path("deletesubcategory", deleteListSubCategory),
    path("createrequirement", createListRequirement),
    path("deleterequirement", deleteListRequirement),
    path("createcourse", createListCourse),
    path("deletecourse", deleteListCourse),
    path("createprereq", createListPrereq),
    path("deleteprereq", deleteListPrereq),
    path("createap", createListAp),
    path("deleteap", deleteListAp),
]
