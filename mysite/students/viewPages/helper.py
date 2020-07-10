from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .homePages import *
from ..dataforms.HelperForms import *
from ..datahelper.students.studentsDataGet import *
from lxml import etree

# --- HELPER DATA ---- 
def requestMyMajors(request):
    data = getMajorList(request)
    xml_response = getXMLString(data, 'majors', 'major') 
    return HttpResponse(xml_response, content_type='text/xml')



# --- HELPER FORMS ---
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
