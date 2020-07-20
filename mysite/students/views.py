from .viewPages.auth import *
from .viewPages.courses import *
from .viewPages.helper import *
from .viewPages.home import *
from django.views.decorators.csrf import csrf_protect
import requests
# Create your views here.

# --- MAIN -----
def main(request):
    return renderHomeA(request, "students/main.html")

def mainCourses(request):
    return renderHomeB(request, "students/main.html")

def mainHelper(request):
    return renderHomeC(request, "students/main.html")

# --- TESTING --- 
def test(request):
    return renderHome(request, "students/main.html")

# --- AUTH OPERATIONS ---
@csrf_protect
def signUpForm(request):
    return signUpFormHelper(request)

def activate(request, uidb64, token):
    return activateHelper(request, uidb64, token)

@csrf_protect
def signInForm(request):
    return signInFormHelper(request)

def signOut(request):
    return signOutHelper(request)

# --- COURSES XML DATA REQUEST ---

def requestCoursesData(request):
    return requestCoursesDataHelper(request) 

# --- HELPER XML DATA REQUESTS ---
def requestMyMajors(request):
    return requestMyMajorsHelper(request)

def requestMyYears(request):
    return requestMyYearsHelper(request)

def requestMySemesters(request, year):
    return requestMySemestersHelper(request, year)

def requestMyCourses(request, year, semester):
    return requestMyCoursesHelper(request, year, semester)

# --- HELPER OPERATIONS ---
@csrf_protect
def addMyMajor(request):
    return MajorFormAdd(request)

@csrf_protect
def deleteMyMajor(request):
    return MajorFormDelete(request)

@csrf_protect
def addMyYear(request):
    return YearFormAdd(request)

@csrf_protect
def deleteMyYear(request):
    return YearFormDelete(request)

@csrf_protect
def addMySemester(request):
    return SemesterFormAdd(request)

@csrf_protect
def deleteMySemester(request):
    return SemesterFormDelete(request)

@csrf_protect
def addMyCourse(request):
    return CourseFormAdd(request)

@csrf_protect
def deleteMyCourse(request):
    return CourseFormDelete(request)
