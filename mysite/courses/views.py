from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *
from .dataforms.coursesAPIData import *


# Create your views here.

# --- view sets ---
class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class PrereqViewSet(viewsets.ModelViewSet):
    queryset = Prereq.objects.all()
    serializer_class = PrereqSerializer


class ApCreditViewSet(viewsets.ModelViewSet):
    queryset = ApCredit.objects.all()
    serializer_class = ApCreditSerializer

# --- COURSES REQUESTS ---
# return XML

def requestMajors(request):
    data = getMajorList(request)
    xml_response = getXMLString(data, 'majors', 'major') 
    return HttpResponse(xml_response, content_type='text/xml')


def requestCategories(request, major_name):
    data = getCategoryList(request, major_name)
    xml_response = getXMLString(data, 'categories', 'category') 
    return HttpResponse(xml_response, content_type='text/xml')
   

def requestSubCategories(request, category_name):
    data = getSubCategoryList(request, category_name)
    xml_response = getXMLString(data, 'subcategories', 'subcategory') 
    return HttpResponse(xml_response, content_type='text/xml') 


def requestRequirements(request, subcategory_name):
    data = getRequirementList(request, subcategory_name)
    xml_response = getXMLString(data, 'requirements', 'requirement') 
    return HttpResponse(xml_response, content_type='text/xml')


def requestCourses(request, requirement_name):
    data = getCourseList(request, requirement_name)
    xml_response = getXMLString(data, 'courses', 'course') 
    return HttpResponse(xml_response, content_type='text/xml')


def requestPrereqs(request, course_name):
    data = getPrereqList(request, course_name)
    xml_response = getXMLString(data, 'prereqs', 'prereq') 
    return HttpResponse(xml_response, content_type='text/xml')


def requestAP(request, course_name):
    data = getAPList(request, course_name)
    xml_response = getXMLString(data, 'ap', 'test') 
    return HttpResponse(xml_response, content_type='text/xml')