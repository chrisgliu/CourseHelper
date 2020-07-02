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

# --- COURSES REQUESTS ---
def requestMajors(request):
    return getMajorList(request)


def requestCategories(request, major_name):
    return getCategoryList(request, major_name)


def requestSubCategories(request, category_name):
    return getSubCategoryList(request, category_name)


def requestRequirements(request, subcategory_name):
    return getRequirementList(request, subcategory_name)


def requestCourses(request, requirement_name):
    return getCourseList(request, requirement_name)


def requestPrereqs(request, course_name):
    return getPrereqList(request, course_name)


def requestAP(request, course_name):
    return getAPList(request, course_name)

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
