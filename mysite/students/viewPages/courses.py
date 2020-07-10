from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from ..dataforms.CoursesForms import *
from ..datahelper.courses.coursesDataGet import *
from ..datahelper.XMLString import *
import requests
from .home import *

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

def requestSubCategoryHelper(request, category_name, subcategory_name):
    links = getSubCategoryLinks(request)
    sub_links = filterLinks(request, links, 'categories', category_name)
    specific_link = findInstanceLink(sub_links, 'subcategory', subcategory_name)
    result = requests.get(specific_link)
    xml_response = getXMLComplex('subcategories', 'subcategory', 
    one_ref='note', one_data=result.json().get('note'))
    return HttpResponse(xml_response, content_type='text/xml') 


def requestRequirementsHelper(request, subcategory_name):
    data = getRequirementList(request, subcategory_name)
    xml_response = getXMLString(data, 'requirements', 'requirement') 
    return HttpResponse(xml_response, content_type='text/xml')

def requestRequirementHelper(request, subcategory_name, requirement_name):
    links = getRequirementLinks(request)
    sub_links = filterLinks(request, links, 'subcategories', subcategory_name)
    specific_link = findInstanceLink(sub_links, 'requirement', requirement_name)
    result = requests.get(specific_link)
    xml_response = getXMLComplex('requirements', 'requirement', 
    one_ref='credit', one_data=result.json().get('credit'))
    return HttpResponse(xml_response, content_type='text/xml') 

def requestCoursesHelper(request, requirement_name):
    data = getCourseList(request, requirement_name)
    xml_response = getXMLString(data, 'courses', 'course') 
    return HttpResponse(xml_response, content_type='text/xml')

def requestCourseHelper(request, requirement_name, course_name):
    links = getCourseLinks(request)
    sub_links = filterLinks(request, links, 'requirements', requirement_name)
    specific_link = findInstanceLink(sub_links, 'course', course_name)
    result = requests.get(specific_link)
    xml_response = getXMLComplex('courses', 'course', 
    one_ref='credit', one_data=result.json().get('credit'))
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
def processForm(request, model_form, command):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = model_form(request.POST)
            if form.is_valid():
                form.process(request, command)
                return HttpResponseRedirect(reverse("main"))
    message = 'Sign in first'
    return renderHome(request, 'students/main.html', {"messages": [message]}) 


def listMajorFormAdd(request):
    return processForm(request, ListMajorForm, 'add')


def listMajorFormDelete(request):
    return processForm(request, ListMajorForm, 'delete')


def listCategoryFormAdd(request):
    return processForm(request, ListCategoryForm, 'add')


def listCategoryFormDelete(request):
    return processForm(request, ListCategoryForm, 'delete')


def listSubCategoryFormAdd(request):
    return processForm(request, ListSubCategoryForm, 'add')


def listSubCategoryFormDelete(request):
    return processForm(request, ListSubCategoryForm, 'delete')


def listRequirementFormAdd(request):
    return processForm(request, ListRequirementForm, 'add')


def listRequirementFormDelete(request):
    return processForm(request, ListRequirementForm, 'delete')


def listCourseFormAdd(request):
    return processForm(request, ListCourseForm, 'add')


def listCourseFormDelete(request):
    return processForm(request, ListCourseForm, 'delete')


def listPrereqFormAdd(request):
    return processForm(request, ListPrereqForm, 'add')


def listPrereqFormDelete(request):
    return processForm(request, ListPrereqForm, 'delete')


def listApFormAdd(request):
    return processForm(request, ListApForm, 'add')


def listApFormDelete(request):
    return processForm(request, ListApForm, 'delete')


