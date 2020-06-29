from rest_framework import serializers
from .models import Major, Category, SubCategory, Requirement, Course, Prereq, ApCredit


# major = serializers.StringRelatedField(many=True)


# --- api serialization/formatting ---
class MajorSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="majors-detail",
                                               lookup_field='major',
                                               read_only=True)

    class Meta:
        model = Major
        fields = ('major', 'url')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="categories-detail",
                                               lookup_field='category',
                                               read_only=True)
    major = serializers.HyperlinkedRelatedField(view_name="majors-detail",
                                                lookup_field='major',
                                                read_only=True)

    class Meta:
        model = Category
        fields = ('category', 'major', 'url')


class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="subcategories-detail",
                                               lookup_field='subcategory',
                                               read_only=True)
    categories = serializers.HyperlinkedRelatedField(view_name="categories-detail",
                                                     lookup_field='category',
                                                     read_only=True,
                                                     many=True)

    class Meta:
        model = SubCategory
        fields = ('subcategory', 'note', 'categories', 'url')


class RequirementSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="requirements-detail",
                                               lookup_field='requirement',
                                               read_only=True)
    subcategories = serializers.HyperlinkedRelatedField(view_name="subcategories-detail",
                                                        lookup_field='subcategory',
                                                        read_only=True,
                                                        many=True)

    class Meta:
        model = Requirement
        fields = ('requirement', 'credit', 'subcategories', 'url')


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="courses-detail",
                                               lookup_field='course',
                                               read_only=True)
    requirements = serializers.HyperlinkedRelatedField(view_name="requirements-detail",
                                                       lookup_field='requirement',
                                                       read_only=True,
                                                       many=True)

    class Meta:
        model = Course
        fields = ('course', 'credit', 'requirements', 'url')


class PrereqSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="prereqs-detail",
                                               lookup_field='prereq',
                                               read_only=True)
    courses = serializers.HyperlinkedRelatedField(view_name="courses-detail",
                                                  lookup_field='course',
                                                  read_only=True,
                                                  many=True)

    class Meta:
        model = Prereq
        fields = ('prereq', 'courses', 'url')


class ApCreditSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="apcredits-detail",
                                               lookup_field='test',
                                               read_only=True)
    courses = serializers.HyperlinkedRelatedField(view_name="courses-detail",
                                                  lookup_field='course',
                                                  read_only=True,
                                                  many=True)

    class Meta:
        model = ApCredit
        fields = ('test', 'scoremin', 'scoremax', 'courses', 'url')
