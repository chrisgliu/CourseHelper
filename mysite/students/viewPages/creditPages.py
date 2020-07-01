from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .homePages import *
from ..datahelper.coursesData import *
from ..dataforms.CreditForms import *
from ..datahelper.studentsDataGet import *


# --- CREDIT DATA ---- 
def getCreditData():
    credit_data = {
        'my_majors': getMajors(),
        'my_years': getYears(),
        'my_semesters': getSemesters(),
        'my_courses': getCourses()
    }
    return credit_data

def requestData(request, 
    major=False, category=False,
    subcategory=False,requirement=False, 
    course=False, prereq=False, ap=False, name=""):
    if major:
        return getMajorList(request)
    if category:
        return getCategoryList(request, name)
    if subcategory:
        return getSubCategoryList(request, name)
    if requirement:
        return getRequirementList(request, name)
    if course:
        return getCourseList(request, name)
    if prereq:
        return getPrereqList(request, name)
    if ap:
        return getAPList(request, name)

# --- CREDIT PLANNER ---
def creditPageHelper(request):
   return renderHome(request, 'students/credit.html')

def processForm(request, model_form, command, redirect_name, template_path, context):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = model_form(request.POST)
            if form.is_valid():
                form.process(request.user, command)
                return HttpResponseRedirect(reverse(redirect_name)) 
    return render(request, template_path, context)


def MajorFormAdd(request):
    return processForm(request, MajorForm, 'add', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


def MajorFormDelete(request):
    return processForm(request, MajorForm, 'delete', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


def YearFormAdd(request):
    return processForm(request, YearForm, 'add', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


def YearFormAdd(request):
    return processForm(request, YearForm, 'delete', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})

def SemesterFormAdd(request):
    return processForm(request, SemesterForm, 'add', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


def SemesterFormDelete(request):
    return processForm(request, SemesterForm, 'delete', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


def CourseFormAdd(request):
    return processForm(request, CourseForm, 'add', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


def CourseFormAdd(request):
    return processForm(request, CourseForm, 'delete', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


