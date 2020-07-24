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
    path("createstudent", createStudent, name='addStudent'),
    path("deletestudent", deleteStudent, name='deleteStudent'),
    path("createenrollkey", createEnroll, name='addEnrollment'),
    path("deleteenrollkey", deleteEnroll, name='deleteEnrollment'),
    path("createmajor", createMajor, name='addMajor'),
    path("deletemajor", deleteMajor, name='deleteMajor'),
    path("createcategory", createCategory, name='addCategory'),
    path("deletecategory", deleteCategory, name='deleteCategory'),
    path("createsubcategory", createSubCategory, name='addSubcategory'),
    path("deletesubcategory", deleteSubCategory, name='deleteSubcategory'),
    path("createrequirement", createRequirement, name='addRequirement'),
    path("deleterequirement", deleteRequirement, name='deleteRequirement'),
    path("createcourse", createCourse, name='addCourse'),
    path("deletecourse", deleteCourse, name='deleteCourse'),
    path("createprereq", createPrereq, name='addPrereq'),
    path("deleteprereq", deletePrereq, name='deletePrereq'),
    path("createap", createAp, name='addAp'),
    path("deleteap", deleteAp, name='deleteAp'),
]
