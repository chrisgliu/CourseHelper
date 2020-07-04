from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .homePages import *
from ..dataforms.CoursesForms import *
from ..datahelper.coursesDataGet import *

# --- COURSES DATA ---- 
def requestMajorsHelper(request):
    data = getMajorList(request)
    xml_response = getXMLString(data, 'majors', 'major') 
    return HttpResponse(xml_response, content_type='text/xml')


def requestCategoriesHelper(request, major_name):
    data = getCategoryList(request, major_name)
    xml_response = getXMLString(data, 'categories', 'category') 
    return HttpResponse(xml_response, content_type='text/xml')
   

def requestSubCategoriesHelper(request, category_name):
    data = getSubCategoryList(request, category_name)
    xml_response = getXMLString(data, 'subcategories', 'subcategory') 
    return HttpResponse(xml_response, content_type='text/xml') 


def requestRequirementsHelper(request, subcategory_name):
    data = getRequirementList(request, subcategory_name)
    xml_response = getXMLString(data, 'requirements', 'requirement') 
    return HttpResponse(xml_response, content_type='text/xml')


def requestCoursesHelper(request, requirement_name):
    data = getCourseList(request, requirement_name)
    xml_response = getXMLString(data, 'courses', 'course') 
    return HttpResponse(xml_response, content_type='text/xml')


def requestPrereqsHelper(request, course_name):
    data = getPrereqList(request, course_name)
    xml_response = getXMLString(data, 'prereqs', 'prereq') 
    return HttpResponse(xml_response, content_type='text/xml')


def requestAPHelper(request, course_name):
    data = getAPList(request, course_name)
    xml_response = getXMLString(data, 'ap', 'test') 
    return HttpResponse(xml_response, content_type='text/xml')


# --- COURSES FORMS ---
def processForm(request, model_form, command, redirect_name, template_path, context):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = model_form(request.POST)
            if form.is_valid():
                form.process(request.user, command)
                return HttpResponseRedirect(reverse(redirect_name)) 
    return render(request, template_path, context)


def listMajorFormAdd(request):
    return processForm(request, ListMajorForm, 'add', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


def listMajorFormDelete(request):
    return processForm(request, ListMajorForm, 'delete', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


def listCategoryFormAdd(request):
    return processForm(request, ListCategoryForm, 'add', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


def listCategoryFormDelete(request):
    return processForm(request, ListCategoryForm, 'delete', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


def listSubCategoryFormAdd(request):
    return processForm(request, ListSubCategoryForm, 'add', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


def listSubCategoryFormDelete(request):
    return processForm(request, ListSubCategoryForm, 'delete', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


def listRequirementFormAdd(request):
    return processForm(request, ListRequirementForm, 'add', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


def listRequirementFormDelete(request):
    return processForm(request, ListRequirementForm, 'delete', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


def listCourseFormAdd(request):
    return processForm(request, ListCourseForm, 'add', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


def listCourseFormDelete(request):
    return processForm(request, ListCourseForm, 'delete', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})

def listPrereqFormAdd(request):
    return processForm(request, ListPrereqForm, 'add', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


def listPrereqFormDelete(request):
    return processForm(request, ListPrereqForm, 'delete', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})

def listApFormAdd(request):
    return processForm(request, ListApForm, 'add', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


def listApFormDelete(request):
    return processForm(request, ListApForm, 'delete', 'credit', 
        'students/signIn.html', {'message': 'Sign in first'})


