from django.urls import path
from . import views

urlpatterns = [
    # --- MAIN -----
    path("", views.main, name="main"),
    # --- TESTING --- 
    path("test", views.test, name="test"),
    # --- AUTH OPERATIONS ---
    path("signUpForm", views.signUpForm, name="signUpForm"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path("signInForm", views.signInForm, name="signInForm"),
    path("signOut", views.signOut, name="signOut"),
    # --- COURSES XML DATA REQUESTS --
    path('requestmajors', views.requestMajors),
    path('requestcategories/<major_name>/', views.requestCategories),
    path('requestsubcategories/<category_name>/', views.requestSubCategories),
    path('requestsubcategory/<category_name>/<subcategory_name>/', views.requestSubCategory).
    path('requestrequirements/<subcategory_name>/', views.requestRequirements),
    path('requestrequirement/<subcategory_name>/<requirement_name>/', views.requestRequirement),
    path('requestcourses/<requirement_name>/', views.requestCourses),
    path('requestcourse/<requirement_name>/<course_name>/', views.requestCourse),
    path('requestprereqs/<course_name>/', views.requestPrereqs),
    path('requestap/<course_name>/', views.requestAP),
    # --- HELPER XML DATA REQUESTS ---
    path('requestmymajors', views.requestMyMajors),
    path('requestmyyears', views.requestMyYears), 
    path('requestmysemesters/<year>/', views.requestMySemesters)
    path('requestmycourses/<semester>', views.requestMyCourses)
    # --- COURSES OPERATIONS ---
    path("addMajor", views.addMajor, name='addMajor'),
    path("deleteMajor", views.deleteMajor, name='deleteMajor'),
    path("addCategory", views.addCategory, name='addCategory'),
    path("deleteCategory", views.deleteCategory, name='deleteCategory'),
    path("addSubcategory", views.addSubCategory, name='addSubcategory'),
    path("deleteSubcategory", views.deleteSubCategory, name='deleteSubcategory'),
    path("addRequirement", views.addRequirement, name='addRequirement'),
    path("deleteRequirement", views.deleteRequirement, name='deleteRequirement'),
    path("addCourse", views.addCourse, name='addCourse'),
    path("deleteCourse", views.deleteCourse, name='deleteCourse'),
    path("addPrereq", views.addPrereq, name='addPrereq'),
    path("deletePrereq", views.deletePrereq, name='deletePrereq'),
    path("addAp", views.addAp, name='addAp'),
    path("deleteAp", views.deleteAp, name='deleteAp'),
    # --- HELPER OPERATIONS ---
    path("addMyMajor", views.addMyMajor, name='addMyMajor'),
    path("deleteMajor", views.deleteMyMajor, name='deleteMyMajor'),
    path("addMyYear", views.addMyYear, name='addMyYear'),
    path("deleteMyYear", views.deleteMyYear, name='deleteMyYear'),
    path("addMySemester", views.addMySemester, name='addMySemester'),
    path("deleteMySemester", views.deleteMySemester, name='deleteMySemester'),
    path("addMyCourse", views.addMyCourse, name='addMyCourse'),
    path("deleteMyCourse", views.deleteMyCourse, name='deleteMyCourse'),
    
]
