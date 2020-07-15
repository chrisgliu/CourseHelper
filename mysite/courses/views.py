from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import *
from .serializers import *
from .models import *
from .datahelper.courseslist import *
from .courses import *

# Create your views here.

# --- view sets ---
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EnrolledViewSet(viewsets.ModelViewSet):
    queryset = Enrolled.objects.all()
    serializer_class = EnrolledSerializer

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

# --- create and delete data ---
def createListStudent(request):
    return listStudentFormAdd(request)

def deleteListStudent(request):
    return listStudentFormDelete;

def createListEnroll(request):
    return listEnrollFormAdd(request);

def deleteListEnroll(request):
    return listEnrollFormDelete(request)

def createListMajor(request):
    return listMajorFormAdd(request)

def deleteListMajor(request):
    return listMajorFormDelete(request)

def createListCategory(request):
    return listCategoryFormAdd(request)

def deleteListCategory(request):
    return listCategoryFormDelete(request)

def createListSubCategory(request):
    return listSubCategoryFormAdd(request)

def deleteListSubCategory(request):
    return listSubCategoryFormDelete(request)

def createListRequirement(request):
    return listRequirementFormAdd(request)

def deleteListRequirement(request):
    return listRequirementFormDelete(request)

def createListCourse(request):
    return listCourseFormAdd(request)

def deleteListCourse(request):
    return listCourseFormDelete(request)

def createListPrereq(request):
    return listPrereqFormAdd(request)

def deleteListPrereq(request):
    return listPrereqFormDelete(request)

def createListAp(request):
    return listApFormAdd(request)

def deleteListAp(request):
    return listApFormDelete(request)

# --- get json data list ---
def requestMajorList(request, username):
    return requestMajorListHelper(request, username)

def requestCategoriesList(request, username, major_name):
    return requestCategoriesListHelper(request, username, major_name)
    
def requestSubcategoriesList(request, username, major_name, category_name):
    return requestSubcategoriesListHelper(request, username, major_name, category_name)   

def requestRequirementsList(request, username, major_name, category_name, subcategory_name):
    return requestRequirementsListHelper(request, username, major_name, category_name, subcategory_name)

def requestCoursesList(request, username, major_name, category_name, subcategory_name, requirement_name):
    return requestCoursesListHelper(request, username, major_name, category_name, subcategory_name, requirement_name)     

def requestPrereqList(request, username, major_name, category_name, subcategory_name, requirement_name, course_name):
    return requestPrereqListHelper(request, username, major_name, category_name, subcategory_name, requirement_name, course_name)
     
def requestApList(request, username, major_name, category_name, subcategory_name, requirement_name, course_name):
    return requestApListHelper(request, username, major_name, category_name, subcategory_name, requirement_name, course_name)

# --- request specific data ---
def requestSubcategoryNote(request, username, major_name, category_name, subcategory_name):
    return requestSubcategoryNoteHelper(request, username, major_name, category_name, subcategory_name)

def requestRequirementCredit(request, username, major_name, category_name, subcategory_name, requirement_name):
    return requestRequirementCreditHelper(request, username, major_name, category_name, subcategory_name, requirement_name)

def requestCoursesCredit(request, username, major_name, category_name, subcategory_name, requirement_name, course_name):
    return requestCoursesCreditHelper(request, username, major_name, category_name, subcategory_name, requirement_name, course_name)

