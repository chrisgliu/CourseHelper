from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *
from .coursesData import *

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
def requestMajors(request):
    return getMajorList(request)


def requestCategories(request, major_name):
    return getCategoryList(request, major_name)


def requestSubCategories(request, category_name):
    return getSubCategoryList(request, category_name)


def requestRequirements(request, subcategory_name):
    return getRequirementList(request, subcategory_name)


def requestCourses(request, requirement_name):
    return getCourseList(request, requirement_name)


def requestPrereqs(request, course_name):
    return getPrereqList(request, course_name)


def requestAP(request, course_name):
    return getAPList(request, course_name)
