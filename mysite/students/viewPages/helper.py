from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from ..dataforms.HelperForms import *
from ..datahelper.students.studentsDataGet import *
from ..datahelper.XMLString import *
from .home import *

# --- HELPER DATA ---- 
def getNames(data_objects, name_attr):
    data = []
    for instance in data_objects:
        name = getattr(instance, name_attr)
        data.append(name)
    return data


def requestMyMajorsHelper(request):
    data_objects = getMajors(request.user)
    data = getNames(data_objects, 'major')    
    xml_response = getXMLString(data, data_set='majors', data_model='major')
    return HttpResponse(xml_response, content_type='text/xml')


def requestMyYearsHelper(request):
    data_objects = getYears(request.user)
    data = getNames(data_objects, 'year')
    xml_response = getXMLString(data, data_set='years', data_model='year')
    return HttpResponse(xml_response, content_type='text/xml')


def requestMySemestersHelper(request, year):
    data_objects = getSemesters(request.user, year)
    data = getNames(data_objects, 'semester')
    xml_response = getXMLString(data, data_set='semesters', data_model='semester')
    return HttpResponse(xml_response, content_type='text/xml')


def requestMyCoursesHelper(request, year, semester):
    data_objects = getCourses(request, year, semester)
    data = getNames(data_objects, 'course')
    xml_response = getXMLString(data, data_set='courses', data_model='course')
    return HttpResponse(xml_response, content_type='text/xml')

# --- HELPER FORMS ---
def processForm(request, model_form, command):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = model_form(request.POST)
            if form.is_valid():
                form.process(request, command)
                return HttpResponseRedirect(reverse("main"))
    message = 'Sign in first'
    return renderHome(request, 'students/main.html', {"messages": [message]}) 


def MajorFormAdd(request):
    return processForm(request, MajorForm, 'add')


def MajorFormDelete(request):
    return processForm(request, MajorForm, 'delete')


def YearFormAdd(request):
    return processForm(request, YearForm, 'add')


def YearFormDelete(request):
    return processForm(request, YearForm, 'delete')


def SemesterFormAdd(request):
    return processForm(request, SemesterForm, 'add')


def SemesterFormDelete(request):
    return processForm(request, SemesterForm, 'delete')


def CourseFormAdd(request):
    return processForm(request, CourseForm, 'add')


def CourseFormDelete(request):
    return processForm(request, CourseForm, 'delete')
