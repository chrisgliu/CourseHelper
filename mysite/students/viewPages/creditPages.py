from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .homePages import *
from ..dataforms.CreditForms import *
from ..datahelper.students.studentsDataGet import *
from ..dataforms.CoursesForms import *

# --- CREDIT PAGE ONE---
def creditPageHelperOne(request):
    courses_forms = {
        'ListMajorForm': ListMajorForm(),
        'ListCategoryForm': ListCategoryForm(),
        'ListSubCategoryForm': ListSubCategoryForm(),
        'ListRequirementForm': ListRequirementForm(),
        'ListCourseForm': ListCourseForm(),
        'ListPrereqForm': ListPrereqForm(),
        'ListApForm': ListApForm(),
    }
    return renderHome(request, 'students/credit_one.html', courses_forms)

# --- CREDIT PAGE TWO ---- 
def getCreditData(request):
    if request.user.is_authenticated:
        years = getYears(request.user)
        semesters_list = {}
        for year in years:
            semesters = getSemesters(request.user, year)
            courses_list = {}
            for semester in semesters:
                courses = getCourses(request.user, year, semester)
                courses_list[semester] = courses
            semesters_list[year] = courses_list
        credit_data = {
            'my_majors': getMajors(request.user),
            'my_years': getYears(request.user),
            'my_semesters': semesters_list
        }
        return credit_data
    return {}

def creditPageHelperTwo(request):
   return renderHome(request, 'students/credit_two.html', getCreditData(request))

# --- CREDIT FORMS ---
def processForm(request, model_form, command, redirect_name, template_path, context):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = model_form(request.POST)
            if form.is_valid():
                form.process(request.user, command)
                return HttpResponseRedirect(reverse(redirect_name)) 
    return render(request, template_path, context)


def MajorFormAdd(request):
    return processForm(request, MajorForm, 'add', 'credit_two', 
        'students/signIn.html', {'message': 'Sign in first'})


def MajorFormDelete(request):
    return processForm(request, MajorForm, 'delete', 'credit_two', 
        'students/signIn.html', {'message': 'Sign in first'})


def YearFormAdd(request):
    return processForm(request, YearForm, 'add', 'credit_two', 
        'students/signIn.html', {'message': 'Sign in first'})


def YearFormDelete(request):
    return processForm(request, YearForm, 'delete', 'credit_two', 
        'students/signIn.html', {'message': 'Sign in first'})


def SemesterFormAdd(request):
    return processForm(request, SemesterForm, 'add', 'credit_two', 
        'students/signIn.html', {'message': 'Sign in first'})


def SemesterFormDelete(request):
    return processForm(request, SemesterForm, 'delete', 'credit_two', 
        'students/signIn.html', {'message': 'Sign in first'})


def CourseFormAdd(request):
    return processForm(request, CourseForm, 'add', 'credit_two', 
        'students/signIn.html', {'message': 'Sign in first'})


def CourseFormDelete(request):
    return processForm(request, CourseForm, 'delete', 'credit_two', 
        'students/signIn.html', {'message': 'Sign in first'})
