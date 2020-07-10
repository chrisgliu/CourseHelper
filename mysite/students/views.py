from .viewPages.auth import *
from .viewPages.courses import *
from .viewPages.helper import *
from .viewPages.home import *
from django.views.decorators.csrf import csrf_protect
import requests
# Create your views here.

# --- MAIN -----
def main(request):
    return renderHome(request, "students/main.html")

# --- TESTING --- 
def test(request):
    return HttpsResponse('hello')

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

# --- COURSES XML DATA REQUESTS ---
def requestMajors(request):
    return requestMajorsHelper(request)

def requestCategories(request, major_name):
    return requestCategoriesHelper(request, major_name)

def requestSubCategories(request, category_name):
    return requestSubCategoriesHelper(request, category_name)

def requestSubCategory(request, category_name, subcategory_name):
    return requestSubCategoryHelper(request, category_name, subcategory_name)

def requestRequirements(request, subcategory_name):
    return requestRequirementsHelper(subcategory_name)

def requestRequirement(request, subcategory_name, requirement_name):
    return requestRequirementHelper(request, subcategory_name, requirement_name)

def requestCourses(request, requirement_name):
    return requestCoursesHelper(request, requirement_name)

def requestCourse(request, requirement_name, course_name):
    return requestCourseHelper(request, requirement_name, course_name)

def requestPrereqs(request, course_name):
    return requestPrereqsHelper(request, course_name)

def requestAP(request, course_name):
    return requestAPHelper(request, course_name)

# --- HELPER XML DATA REQUESTS ---
def requestMyMajors(request):
    return requestMyMajorsHelper(request)

def requestMyYears(request):
    return requestMyYearsHelper(request)

def requestMySemesters(request, year):
    return requestMySemestersHelper(request, year)

def requestMyCourses(request, semester):
    return requestMyCoursesHelper(request, semester)

# --- COURSES OPERATIONS ---
@csrf_protect
def addMajor(request):
    return listMajorFormAdd(request)

@csrf_protect
def deleteMajor(request):
    return listMajorFormDelete(request)

@csrf_protect
def addCategory(request):
    return listCategoryFormAdd(request)
    
@csrf_protect
def deleteCategory(request):
    return listCategoryFormDelete(request)

@csrf_protect
def addSubCategory(request):
    return listSubCategoryFormAdd(request)
    
@csrf_protect
def deleteSubCategory(request):
    return listSubCategoryFormDelete(request)

@csrf_protect
def addRequirement(request):
    return listRequirementFormAdd(request)
    
@csrf_protect
def deleteRequirement(request):
    return listRequirementFormDelete(request)

@csrf_protect
def addCourse(request):
    return listCourseFormAdd(request)
    
@csrf_protect
def deleteCourse(request):
    return listCourseFormDelete(request)

@csrf_protect
def addPrereq(request):
    return listPrereqFormAdd(request)
    
@csrf_protect
def deletePrereq(request):
    return listPrereqFormDelete(request)

@csrf_protect
def addAp(request):
    return listApFormAdd(request)
    
@csrf_protect
def deleteAp(request):
    return listApFormDelete(request)

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
