from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *
from .datahelper.courseslist import *
from .courses import *
from django.views.decorators.csrf import csrf_protect

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
@csrf_protect
def createStudent(request):
    return CourseStudentFormAdd(request)
@csrf_protect
def deleteStudent(request):
    return CourseStudentFormDelete(request)
@csrf_protect
def createEnroll(request):
    return CourseEnrollFormAdd(request);
@csrf_protect
def deleteEnroll(request):
    return CourseEnrollFormDelete(request)
@csrf_protect
def createMajor(request):
    return CourseMajorFormAdd(request)
@csrf_protect
def deleteMajor(request):
    return CourseMajorFormDelete(request)
@csrf_protect
def createCategory(request):
    return CourseCategoryFormAdd(request)
@csrf_protect
def deleteCategory(request):
    return CourseCategoryFormDelete(request)
@csrf_protect
def createSubCategory(request):
    return CourseSubCategoryFormAdd(request)
@csrf_protect
def deleteSubCategory(request):
    return CourseSubCategoryFormDelete(request)
@csrf_protect
def createRequirement(request):
    return CourseRequirementFormAdd(request)
@csrf_protect
def deleteRequirement(request):
    return CourseRequirementFormDelete(request)
@csrf_protect
def createCourse(request):
    return CourseCourseFormAdd(request)
@csrf_protect
def deleteCourse(request):
    return CourseCourseFormDelete(request)
@csrf_protect
def createPrereq(request):
    return CoursePrereqFormAdd(request)
@csrf_protect
def deletePrereq(request):
    return CoursePrereqFormDelete(request)
@csrf_protect
def createAp(request):
    return CourseApFormAdd(request)
@csrf_protect
def deleteAp(request):
    return CourseApFormDelete(request)

# --- get json data Course ---
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

