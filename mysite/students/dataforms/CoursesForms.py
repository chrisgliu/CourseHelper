from django.forms import ModelForm
from django import forms
from ..datahelper.courses.coursesDataAdd import *
from ..datahelper.courses.coursesDataDelete import *
# --- note ---
# does not work with duplicate names in sections
# --- COURSES DATA ---
class ListMajorForm(forms.Form):
    major = forms.CharField(label='major', required=True) 
   
    def process(self, request, add_or_delete='add'):
        major = self.cleaned_data.get('major')
        if add_or_delete == 'add':
            addListMajor(request, major)
        if add_or_delete == 'delete':
            deleteListMajor(request, major)


class ListCategoryForm(forms.Form):
    major = forms.CharField(label='major', required=True)  
    category = forms.CharField(label='category', required=True) 
    
    def process(self, request, add_or_delete='add'):
        major = self.cleaned_data.get('major')
        category = self.cleaned_dat.get('category')
        if add_or_delete == 'add':
            addListCategory(request, major, category)
        if add_or_delete == 'delete':
            deleteListCategory(request, major, category)


class ListSubCategoryForm(forms.Form):
    category = forms.CharField(label='category', required=True)
    subcategory = forms.CharField(label='subcategory', required=True)

    def process(self, request, add_or_delete='add'):
        category = self.cleaned_data.get('category')
        subcategory = self.cleaned_data.get('subcategory')
        if add_or_delete == 'add':
            addListSubCategory(request, category, subcategory)
        if add_or_delete == 'delete':
            deleteListSubCategory(request, category, subcategory)


class ListRequirementForm(forms.Form):
    subcategory = forms.CharField(label='subcategory', required=True)
    requirement = forms.CharField(label='requirement', required=True)

    def process(self, request, add_or_delete='add'):
        subcategory = self.clean_data.get('subcategory')
        requirement = self.cleaned_data.get('requirement')
        if add_or_delete == 'add':
            addListRequirement(request, subcategory, requirement)
        if add_or_delete == 'delete':
            deleteListRequirement(request, subcategory, requirement)


class ListCourseForm(forms.Form):
    requirement = forms.CharField(label='requirement', required=True)
    course = forms.CharField(label='course', required=True)

    def process(self, request, add_or_delete='add'):
        requirement = self.clean_data.get('requirement')
        course = self.cleaned_data.get('course')
        if add_or_delete == 'add':
            addListCourses(request, requirement, course)
        if add_or_delete == 'delete':
            deleteListCourses(request, requirement, course)


class ListPrereqForm(forms.Form):
    course = forms.CharField(label='course', required=True)
    prereq = forms.CharField(label='prereq', required=True)

    def process(self, request, add_or_delete='add'):
        course = self.cleaned_data.get('course')
        prereq = self.clean_data.get('prereq')
        if add_or_delete == 'add':
            addListPrereq(request, course, prereq)
        if add_or_delete == 'delete':
            deleteListPrereq(request, course, prereq)


class ListApForm(forms.Form):
    course = forms.CharField(label='course', required=True)
    test = forms.CharField(label='test', required=True)

    def process(self, request, add_or_delete='add'):
        course = self.cleaned_data.get('course')
        test = self.clean_data.get('test')
        if add_or_delete == 'add':
            addListAp(request, course, test)
        if add_or_delete == 'delete':
            deleteListAp(request, course, test)

