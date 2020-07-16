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
    path("createstudent", createListStudent, name='addStudent'),
    path("deletestudent", deleteListStudent, name='deleteStudent'),
    path("createenrollkey", createListEnroll, name='addEnrollment'),
    path("deleteenrollkey", deleteListEnroll, name='deleteEnrollment'),
    path("createmajor", createListMajor, name='addMajor'),
    path("deletemajor", deleteListMajor, name='deleteMajor'),
    path("createcategory", createListCategory, name='addCategory'),
    path("deletecategory", deleteListCategory, name='deleteCategory'),
    path("createsubcategory", createListSubCategory, name='addSubcategory'),
    path("deletesubcategory", deleteListSubCategory, name='deleteSubcategory'),
    path("createrequirement", createListRequirement, name='addRequirement'),
    path("deleterequirement", deleteListRequirement, name='deleteRequirement'),
    path("createcourse", createListCourse, name='addCourse'),
    path("deletecourse", deleteListCourse, name='deleteCourse'),
    path("createprereq", createListPrereq, name='addPrereq'),
    path("deleteprereq", deleteListPrereq, name='deletePrereq'),
    path("createap", createListAp, name='addAp'),
    path("deleteap", deleteListAp, name='deleteAp'),
]
