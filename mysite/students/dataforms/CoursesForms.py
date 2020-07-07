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
        category = self.cleaned_data.get('category')
        if add_or_delete == 'add':
            addListCategory(request, major, category)
        if add_or_delete == 'delete':
            deleteListCategory(request, major, category)


class ListSubCategoryForm(forms.Form):
    category = forms.CharField(label='category', required=True)
    subcategory = forms.CharField(label='subcategory', required=True)
    note = forms.CharField(label='note', required=False)

    def process(self, request, add_or_delete='add'):
        category = self.cleaned_data.get('category')
        subcategory = self.cleaned_data.get('subcategory')
        note = self.cleaned_data.get('note')
        if add_or_delete == 'add':
            addListSubCategory(request, category, subcategory, note)
        if add_or_delete == 'delete':
            deleteListSubCategory(request, category, subcategory)


class ListRequirementForm(forms.Form):
    subcategory = forms.CharField(label='subcategory', required=True)
    requirement = forms.CharField(label='requirement', required=True)
    credit = forms.IntegerField(label='credit', required=False)

    def process(self, request, add_or_delete='add'):
        subcategory = self.cleaned_data.get('subcategory')
        requirement = self.cleaned_data.get('requirement')
        credit = self.cleaned_data.get('credit')
        if add_or_delete == 'add':
            addListRequirement(request, subcategory, requirement, credit)
        if add_or_delete == 'delete':
            deleteListRequirement(request, subcategory, requirement)


class ListCourseForm(forms.Form):
    requirement = forms.CharField(label='requirement', required=True)
    course = forms.CharField(label='course', required=True)
    credit = forms.IntegerField(label='credit', required=False)

    def process(self, request, add_or_delete='add'):
        requirement = self.cleaned_data.get('requirement')
        course = self.cleaned_data.get('course')
        credit = self.cleaned_data.get('credit')
        if add_or_delete == 'add':
            addListCourses(request, requirement, course, credit)
        if add_or_delete == 'delete':
            deleteListCourses(request, requirement, course)


class ListPrereqForm(forms.Form):
    course = forms.CharField(label='course', required=True)
    prereq = forms.CharField(label='prereq', required=True)

    def process(self, request, add_or_delete='add'):
        course = self.cleaned_data.get('course')
        prereq = self.cleaned_data.get('prereq')
        if add_or_delete == 'add':
            addListPrereq(request, course, prereq)
        if add_or_delete == 'delete':
            deleteListPrereq(request, course, prereq)


class ListApForm(forms.Form):
    course = forms.CharField(label='course', required=True)
    test = forms.CharField(label='test', required=True)
    scoremin = forms.IntegerField(label='scoremin', required=True)
    scoremax = forms.IntegerField(label='scoremax', required=True)

    def process(self, request, add_or_delete='add'):
        course = self.cleaned_data.get('course')
        test = self.cleaned_data.get('test')
        scoremin = self.cleaned_data.get('scoremin')
        scoremax = self.cleaned_data.get('scoremax')
        if add_or_delete == 'add':
            addListAp(request, course, test, scoremin, scoremax)
        if add_or_delete == 'delete':
            deleteListAp(request, course, test, scoremin, scoremax)

