from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import MajorSerializer, CategorySerializer, SubCategorySerializer, RequirementSerializer, CourseSerializer, PrereqSerializer, ApCreditSerializer
from .models import Major, Category, SubCategory, Requirement, Course, Prereq, ApCredit

# Create your views here.	

# --- view sets ---
class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all().order_by('pk')
    serializer_class = MajorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('pk')
    serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all().order_by('pk')
    serializer_class = SubCategorySerializer

class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all().order_by('pk')
    serializer_class = RequirementSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('pk')
    serializer_class = CourseSerializer

class PrereqViewSet(viewsets.ModelViewSet):
    queryset = Prereq.objects.all().order_by('pk')
    serializer_class = PrereqSerializer

class ApCreditViewSet(viewsets.ModelViewSet):
    queryset = ApCredit.objects.all().order_by('pk')
    serializer_class = ApCreditSerializer