from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from ..dataforms.CoursesForms import *
from ..datahelper.courses.coursesDataGet import *
from lxml import etree
import requests
from .home import *

# --- COURSES DATA ---- 

def requestCoursesDataHelper(request):
    root = etree.Element('coursesdata')
    for major in getMajorList(request):
        major_item = etree.Element('major')
        major_name = etree.Element('major_name')
        major_name.text = major
        major_item.append(major_name)
        categories = etree.Element('categories')
        for category in getCategoryList(request, major):
            category_item = etree.Element('category')
            category_name = etree.Element('category_name')
            category_name.text = category
            category_item.append(category_name)
            subcategories = etree.Element('subcategories')
            for subcategory in getSubCategoryList(request, major, category):
                subcategory_item = etree.Element('subcategory')
                subcategory_name = etree.Element('subcategory_name')
                subcategory_name.text = subcategory
                subcategory_item.append(subcategory_name)
                subcategory_data = etree.Element('subcategory_data')
                subcategory_data.text = getSubCategoryNote(request, major, category, subcategory)
                subcategory_item.append(subcategory_data)
                requirements = etree.Element('requirements')
                for requirement in getRequirementList(request, major, category, subcategory):
                    requirement_item = etree.Element('requirement')
                    requirement_name = etree.Element('requirement_name')
                    requirement_name.text = requirement
                    requirement_item.append(requirement_name)
                    requirement_data = etree.Element('requirement_data')
                    requirement_data.text = getRequirementCredit(request, major, category, subcategory, requirement)
                    requirement_item.append(requirement_data)
                    courses = etree.Element('courses')
                    for course in getCourseList(request, major, category, subcategory, requirement):
                        course_item = etree.Element('course')
                        course_name = etree.Element('course_name')
                        course_name.text = course
                        course_item.append(course_name)
                        course_data = etree.Element('course_data')
                        course_data.text = getCourseCredit(request, major, category, subcategory, requirement, course)
                        course_item.append(course_data)
                        prereqs = etree.Element('prereqs')
                        ap = etree.Element('ap')
                        for prereq in getPrereqList(request, major, category, subcategory, requirement, course):
                            prereq_item = etree.Element('prereq')
                            prereq_name = etree.Element('prereq_name')
                            prereq_name.text = prereq
                            prereq_item.append(prereq_name)
                            prereqs.append(prereq_item)
                        for test in getAPList(request, major, category, subcategory, requirement, course):
                            test_item = etree.Element('test')
                            test_name = etree.Element('test_name')
                            test_name.text = test
                            test_item.append(test_name)
                            ap.append(test_item)
                        course_item.append(prereqs)
                        course_item.append(ap)
                        courses.append(course_item)
                    requirement_item.append(courses)
                    requirements.append(requirement_item)
                subcategory_item.append(requirements)
                subcategories.append(subcategory_item)
            category_item.append(subcategories)
            categories.append(category_item)
        major_item.append(categories)
        root.append(major_item)
    xml_response = etree.tostring(root, xml_declaration=True)
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


