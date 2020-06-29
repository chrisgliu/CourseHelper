from rest_framework import serializers
from .models import Major, Category, SubCategory, Requirement, Course, Prereq, ApCredit


# --- api serialization/formatting ---
class MajorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class RequirementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Requirement
        fields = '__all__'


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class PrereqSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prereq
        fields = '__all__'


class ApCreditSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApCredit
        fields = '__all__'
