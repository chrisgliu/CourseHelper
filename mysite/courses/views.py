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
   