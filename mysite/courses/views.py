from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import *
from .serializers import *
from .models import *


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

# --- manipulate relationships ---
def linkStudentAndEnrollment(request, student_pk, enrollment_pk):
    student = Student.objects.get(pk=student_pk)
    enrolled = Enrolled.objects.get(pk=enrollment_pk)
    enrolled.students = student
    enrolled.save()

def linkEnrollmentAndMajor(request, enrollment_pk, major_pk):
    enrolled = Enrolled.objects.get(pk=enrollment_pk)
    major = Major.objects.get(pk=major_pk)
    major.enrolled.add(enrolled)
    major.save()

def linkMajorAndCategory(request, major_pk, category_pk):
    major = Major.objects.get(pk=major_pk)
    category = Category.objects.get(pk=category_pk)
    category.major.add(major)
    category.save()

def linkCategoryAndSubcategory(request, category_pk, subcategory_pk):
    category = Category.objects.get(pk=category_pk)
    subcategory = SubCategory.objects.get(pk=subcategory_pk)
    subcategory.categories.add(category) 
    subcategory.save()

def linkSubcategoryAndRequirement(request, subcategory_pk, requirement_pk):
    subcategory = SubCategory.objects.get(pk=subcategory_pk)
    requirement = Requirement.objects.get(pk=requirement_pk)
    requirement.subcategories.add(subcategory) 
    requirement.save()

def linkRequirementAndCourse(request, requirement_pk, course_pk):
    requirement = Requirement.objects.get(pk=requirement_pk)
    course = Course.objects.get(pk=course_pk)
    course.requirements.add(requirement)
    course.save()

def linkCourseAndPrereq(request, course_pk, prereq_pk):
    course = Course.objects.get(pk=course_pk)
    prereq = Prereq.objects.get(pk=prereq_pk)
    prereq.courses.add(course)
    prereq.save()

def linkCourseAndAp(request, course_pk, ap_pk):
    course = Course.objects.get(pk=course_pk)
    test = ApCredit.objects.get(pk=ap_pk)
    test.courses.add(course)
    test.save()
