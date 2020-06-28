from django.urls import path
from . import views

urlpatterns = [
    # about
    path("about", views.aboutpage, name="about"),
    # main pages
    path("", views.creditpage, name="credit"),
    path("sched", views.schedpage, name="sched"),
    path("budget", views.budgetpage, name="budget"),
    # main forms
    path("creditform", views.creditform, name="creditform"),
    path("schedform", views.schedform, name="schedform"),
    path("budgetform", views.budgetform, name="budgetform"),
    # user
    path("signup", views.signuppage, name="signup"),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path("signin", views.signinpage, name="signin"),
    path("signout", views.signout, name="signout"),
    # user forms 
    path("signupform", views.signupform, name="signupform"),
    path("signinform", views.signinform, name="signinform"),
    # for testing
    path("test", views.test, name="test"),
    
]
