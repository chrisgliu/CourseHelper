from django.urls import path
from . import views

urlpatterns = [
    # for testing
    path("test", views.test, name="test"),
    # about
    path("about", views.aboutPage, name="about"),
    # user
    path("signUp", views.signUpPage, name="signUp"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path("signIn", views.signInPage, name="signIn"),
    path("signOut", views.signOut, name="signOut"),
    # user Forms 
    path("signUpForm", views.signUpForm, name="signUpForm"),
    path("signInForm", views.signInForm, name="signInForm"),
    # main Pages
    path("", views.creditPage, name="credit"),
    path("schedule", views.schedulePage, name="schedule"),
    path("budget", views.budgetPage, name="budget"),
    # # main Forms
    # path("creditForm", views.creditForm, name="creditForm"),
    # path("ScheduleForm", views.scheduleForm, name="scheduleForm"),
    # path("budgetForm", views.budgetForm, name="budgetForm"),  
    # courses requests
    path('requestmajors/', views.requestMajors, name='request_majors'),
    path('requestcategories/<major_name>/', views.requestCategories, name='request_categories'),
    path('requestsubcategories/<category_name>/', views.requestSubCategories, name='request_subcategories'),
    path('requestrequirements/<subcategory_name>/', views.requestRequirements, name='request_requirements'),
    path('requestcourses/<requirement_name>/', views.requestCourses, name='request_courses'),
    path('requestprereqs/<course_name>/', views.requestPrereqs, name='request_prereqs'),
    path('requestap/<course_name>/', views.requestAP, name='request_ap'), 
]
