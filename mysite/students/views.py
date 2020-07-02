from .viewPages.authPages import *
from .viewPages.budgetPages import *
from .viewPages.creditPages import *
from .viewPages.homePages import *
from .viewPages.schedulePages import *
from django.views.decorators.csrf import csrf_protect
from .datahelper.coursesData import *

# Create your views here.

# --- TESTING --- 
def test(request):
    return HttpResponse("Helllo World")

# --- ABOUT ---
def aboutPage(request):
    return renderHome(request, "students/about.html")

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

# --- HOME PAGES ---
def creditPage(request):
    return creditPageHelper(request)


def schedulePage(request):
    return schedulePageHelper(request)


def budgetPage(request):
    return budgetPageHelper(request)

# --- CREDIT FORMS ---
@csrf_protect
def creditAddMajor(request):
    return MajorFormAdd(request)

@csrf_protect
def creditDeleteMajor(request):
    return MajorFormDelete(request)

@csrf_protect
def creditAddYear(request):
    return YearFormAdd(request)

@csrf_protect
def creditDeleteYear(request):
    return YearFormDelete(request)

@csrf_protect
def creditAddSemester(request):
    return SemesterFormAdd(request)

@csrf_protect
def creditDeleteSemester(request):
    return SemesterFormDelete(request)

@csrf_protect
def creditAddCourse(request):
    return CourseFormAdd(request)

@csrf_protect
def creditDeleteCourse(request):
    return CourseFormDelete(request)

# --- SCHEDULE FORMS ---
@csrf_protect
def scheduleForm(request):
    pass

# ---- BUDGET FORMS ---
@csrf_protect
def budgetForm(request):
    pass

