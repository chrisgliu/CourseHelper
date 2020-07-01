from .viewPages.authPages import *
from .viewPages.budgetPages import *
from .viewPages.creditPages import *
from .viewPages.homePages import *
from .viewPages.schedulePages import *
from django.views.decorators.csrf import csrf_protect

# Create your views here.


# --- TESTING --- 
def test(request):
    return HttpResponse("Helllo World")


# --- ABOUT ---
def aboutPage(request):
    return renderHome(request, "students/about.html")

# --- HOME PAGES ---
def creditPage(request):
    return creditPageHelper(request)


def schedulePage(request):
    return schedulePageHelper(request)


def budgetPage(request):
    return budgetPageHelper(request)

# --- FORMS ---
@csrf_protect
def creditForm(request):
    pass


@csrf_protect
def scheduleForm(request):
    pass


@csrf_protect
def budgetForm(request):
    pass


# --- AUTH ---
def signUpPage(request):
    return signUpPageHelper(request)


def signInPage(request):
    return signInPageHelper(request)


def signOut(request):
    return signOutHelper(request)


def activate(request, uidb64, token):
    return activateHelper(request, uidb64, token)


# --- AUTH FORMS ---
@csrf_protect
def signInForm(request):
    return signInFormHelper(request)


@csrf_protect
def signUpForm(request):
    return signUpFormHelper(request)
