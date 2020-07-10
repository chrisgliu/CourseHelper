from django.urls import path
from . import views

urlpatterns = [
    # main Pages
    path("", views.main, name="main"),
    # for testing
    path("test", views.test, name="test"),
    # user 
    path("signUpForm", views.signUpForm, name="signUpForm"),
    path("signInForm", views.signInForm, name="signInForm"),
    path("signOut", views.signOut, name="signOut"),




    # user
    path("signUp", views.signUpPage, name="signUp"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path("signIn", views.signInPage, name="signIn"),
    ,
    
    # credit forms
    path("addMajor", views.creditAddMajor, name='addMajor'),
    path("deleteMajor", views.creditDeleteMajor, name='deleteMajor'),
    path("addYear", views.creditAddYear, name='addYear'),
    path("deleteYear", views.creditDeleteYear, name='deleteYear'),
    path("addSemester", views.creditAddSemester, name='addSemester'),
    path("deleteSemester", views.creditDeleteSemester, name='deleteSemester'),
    path("addCourse", views.creditAddCourse, name='addCourse'),
    path("deleteCourse", views.creditDeleteCourse, name='deleteCourse'),
    # courses requests
    path('requestmajors/', views.requestMajors, name='request_majors'),
    path('requestcategories/<major_name>/', views.requestCategories, name='request_categories'),
    path('requestsubcategories/<category_name>/', views.requestSubCategories, name='request_subcategories'),
    path('requestrequirements/<subcategory_name>/', views.requestRequirements, name='request_requirements'),
    path('requestcourses/<requirement_name>/', views.requestCourses, name='request_courses'),
    path('requestprereqs/<course_name>/', views.requestPrereqs, name='request_prereqs'),
    path('requestap/<course_name>/', views.requestAP, name='request_ap'),
    # courses forms 
    path("addListMajor", views.coursesAddMajor, name='addListMajor'),
    path("deleteListMajor", views.coursesDeleteMajor, name='deleteListMajor'),
    path("addListCategory", views.coursesAddCategory, name='addListCategory'),
    path("deleteListCategory", views.coursesDeleteCategory, name='deleteListCategory'),
    path("addListSubcategory", views.coursesAddSubCategory, name='addListSubcategory'),
    path("deleteListSubcategory", views.coursesDeleteSubCategory, name='deleteListSubcategory'),
    path("addListRequirement", views.coursesAddRequirement, name='addListRequirement'),
    path("deleteListRequirement", views.coursesDeleteRequirement, name='deleteListRequirement'),
    path("addListCourse", views.coursesAddCourse, name='addListCourse'),
    path("deleteListCourse", views.coursesDeleteCourse, name='deleteListCourse'),
    path("addListPrereq", views.coursesAddPrereq, name='addListPrereq'),
    path("deleteListPrereq", views.coursesDeletePrereq, name='deleteListPrereq'),
    path("addListAp", views.coursesAddAp, name='addListAp'),
    path("deleteListAp", views.coursesDeleteAp, name='deleteListAp'),
]
