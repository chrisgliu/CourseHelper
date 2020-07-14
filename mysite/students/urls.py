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
    # --- COURSES XML DATA REQUEST --
    path('requestcoursesdata', views.requestCoursesData, name='courseData'),
    # --- HELPER XML DATA REQUESTS ---
    path('requestmymajors', views.requestMyMajors),
    path('requestmyyears', views.requestMyYears), 
    path('requestmysemesters/<year>/', views.requestMySemesters),
    path('requestmycourses/<year>/<semester>/', views.requestMyCourses),
    # --- COURSES OPERATIONS ---
    path("addMajor", views.addCoursesMajor, name='addMajor'),
    path("deleteMajor", views.deleteCoursesMajor, name='deleteMajor'),
    path("addCategory", views.addCoursesCategory, name='addCategory'),
    path("deleteCategory", views.deleteCoursesCategory, name='deleteCategory'),
    path("addSubcategory", views.addCoursesSubCategory, name='addSubcategory'),
    path("deleteSubcategory", views.deleteCoursesSubCategory, name='deleteSubcategory'),
    path("addRequirement", views.addCoursesRequirement, name='addRequirement'),
    path("deleteRequirement", views.deleteCoursesRequirement, name='deleteRequirement'),
    path("addCourse", views.addCoursesCourse, name='addCourse'),
    path("deleteCourse", views.deleteCoursesCourse, name='deleteCourse'),
    path("addPrereq", views.addCoursesPrereq, name='addPrereq'),
    path("deletePrereq", views.deleteCoursesPrereq, name='deletePrereq'),
    path("addAp", views.addCoursesAp, name='addAp'),
    path("deleteAp", views.deleteCoursesAp, name='deleteAp'),
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
