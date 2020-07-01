from rest_framework import serializers
from .models import *


# major = serializers.StringRelatedField(many=True)


# --- api serialization/formatting ---
class MajorSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="majors-detail",
                                               read_only=True)

    class Meta:
        model = Major
        fields = ('pk', 'major', 'url')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="categories-detail",
                                               read_only=True)
    major = serializers.HyperlinkedRelatedField(view_name="majors-detail",
                                                read_only=True)

    class Meta:
        model = Category
        fields = ('pk', 'category', 'major', 'url')


class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="subcategories-detail",
                                               read_only=True)
    categories = serializers.HyperlinkedRelatedField(view_name="categories-detail",
                                                     read_only=True,
                                                     many=True)

    class Meta:
        model = SubCategory
        fields = ('pk', 'subcategory', 'note', 'categories', 'url')


class RequirementSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="requirements-detail",
                                               read_only=True)
    subcategories = serializers.HyperlinkedRelatedField(view_name="subcategories-detail",
                                                        read_only=True,
                                                        many=True)

    class Meta:
        model = Requirement
        fields = ('pk','requirement', 'credit', 'subcategories', 'url')


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="courses-detail",
                                               read_only=True)
    requirements = serializers.HyperlinkedRelatedField(view_name="requirements-detail",
                                                       read_only=True,
                                                       many=True)

    class Meta:
        model = Course
        fields = ('pk', 'course', 'credit', 'requirements', 'url')


class PrereqSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="prereqs-detail",
                                               read_only=True)
    courses = serializers.HyperlinkedRelatedField(view_name="courses-detail",
                                                  read_only=True,
                                                  many=True)

    class Meta:
        model = Prereq
        fields = ('pk', 'prereq', 'courses', 'url')


class ApCreditSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="apcredits-detail",
                                               read_only=True)
    courses = serializers.HyperlinkedRelatedField(view_name="courses-detail",
                                                  read_only=True,
                                                  many=True)

    class Meta:
        model = ApCredit
        fields = ('pk', 'test', 'scoremin', 'scoremax', 'courses', 'url')
