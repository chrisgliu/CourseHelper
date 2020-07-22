from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from ..dataforms.HelperForms import *
from ..datahelper.students.studentsDataGet import *
from .home import *
from lxml import etree

# majors
# --- progress calculated from front --0
# planner, year and semester/term
# sched, term and courses
# tranfer, test score and courses

# --- HELPER DATA ---- 
def requestMyMajorsHelper(request):
    root = etree.Element('majors')
    data_objects = getMajors(request)
    for major in data_objects:
        major_item = etree.Element('major')
        major_item.text = str(major)
        root.append(major_item)
    xml_response = etree.tostring(root, xml_declaration=True)
    return HttpResponse(xml_response, content_type='text/xml')

def requestMyPlannerHelper(request):
    root = etree.Element('planner')
    year_data_objects = getYears(request)
    for year in year_data_objects:
        year_item = etree.Element('year')
        year_name = etree.Element('year_name')
        year_name.text = str(year)
        year_item.append(year_name)
        semesters = etree.Element('semesters')
        semester_data_objects = getSemesters(request, year)
        for semester in  semester_data_objects:
            semester_item = etree.Element('semester')
            semester_name = etree.Element('semester_name')
            semester_name.text = str(semester)
            semester_item.append(semester_name)
            semesters.append(semester_item)
        if len(semesters):
            year_item.append(semesters)
        root.append(year_item)
    xml_response = etree.tostring(root, xml_declaration=True)
    return HttpResponse(xml_response, content_type='text/xml')

def requestMyScheduleHelper(request):
    root = etree.Element('schedules')
    year_data_objects = getYears(request)
    for year in year_data_objects:
        semester_data_objects = getSemesters(request, year.year)
        for semester in semester_data_objects:
            schedule_item = etree.Element('schedule')
            schedule_name = etree.Element('schedule_name')
            schedule_name.text = str(semester)
            schedule_item.append(schedule_name)
            courses = etree.Element('courses')
            course_data_objects = getCourses(request, year.year, semester.semester)
            for course in course_data_objects:
                course_item = etree.Element('course')
                course_name = etree.Element('course_name')
                course_name.text = str(course)
                course_item.append(course_name)
                courses.append(course_item)
            if len(courses):
                schedule_item.append(courses)
        root.append(schedule_item)
    xml_response = etree.tostring(root, xml_declaration=True)
    return HttpResponse(xml_response, content_type='text/xml')

def requestMyTranferCreditHelper(request):
    root = etree.Element('ap')
    ap_data_objects = getAP(request)
    for test_object in ap_data_objects:
        test_item = etree.Element('test')
        test_name = etree.Element('test_name')
        test_name.text = test_object.test
        test_score = etree.Element('test_score')
        test_score.text = str(test_object.score)
        test_item.append(test_name)
        test_item.append(test_score)
        root.append(test_item)
    xml_response = etree.tostring(root, xml_declaration=True)
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

def APFormAdd(request):
    return processForm(request, APForm, 'add')


def APFormDelete(request):
    return processForm(request, APForm, 'delete')



def SemesterFormAdd(request):
    return processForm(request, SemesterForm, 'add')


def SemesterFormDelete(request):
    return processForm(request, SemesterForm, 'delete')


def CourseFormAdd(request):
    return processForm(request, CourseForm, 'add')


def CourseFormDelete(request):
    return processForm(request, CourseForm, 'delete')
