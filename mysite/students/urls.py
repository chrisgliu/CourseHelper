from django.urls import path
from . import views

urlpatterns = [
    # the main page
    path("", views.index, name="index"),
    # routes to user functions
    path("signup", views.signup, name="signup"),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path("signin", views.signin, name="signin"),
    path("signout", views.signout, name="signout"),
    # for testing
    path("test", views.test, name="test"),
]
