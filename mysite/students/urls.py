from django.urls import path
from . import views

urlpatterns = [
    # --- MAIN -----
    path("", views.main, name="main"),
    path("mycourses", views.mainCourses, name="mainCourses"),
    path("myhelper", views.mainHelper, name='mainHelper'),
    # --- TESTING --- 
    path("test", views.test, name="test"),
    # --- AUTH OPERATIONS ---
    path("account", views.signUpForm, name="signUpForm"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path("signIn", views.signInForm, name="signInForm"),
    path("signOut", views.signOut, name="signOut"),
    # --- COURSES XML DATA REQUEST --
    path('requestcoursesdata', views.requestCoursesData, name='courseData'),
    # --- HELPER XML DATA REQUESTS ---
    path('requestmymajors', views.requestMyMajors),
    path('requestmyyears', views.requestMyYears), 
    path('requestmysemesters/<year>/', views.requestMySemesters),
    path('requestmycourses/<year>/<semester>/', views.requestMyCourses),
    # --- COURSES OPERATIONS ---
    # go to courses app
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
