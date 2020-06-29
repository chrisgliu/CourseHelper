from django.urls import path
from . import views

urlpatterns = [
    # about
    path("about", views.aboutPage, name="about"),
    # main Pages
    path("", views.creditPage, name="credit"),
    path("schedule", views.schedulePage, name="schedule"),
    path("budget", views.budgetPage, name="budget"),
    # main Forms
    path("creditForm", views.creditForm, name="creditForm"),
    path("ScheduleForm", views.scheduleForm, name="scheduleForm"),
    path("budgetForm", views.budgetForm, name="budgetForm"),
    # user
    path("signUp", views.signUpPage, name="signUp"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path("signIn", views.signInPage, name="signIn"),
    path("signOut", views.signOut, name="signOut"),
    # user Forms 
    path("signUpForm", views.signUpForm, name="signUpForm"),
    path("signInForm", views.signInForm, name="signInForm"),
    # for testing
    path("test", views.test, name="test"),
    
]
