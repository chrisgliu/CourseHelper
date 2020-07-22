from django import forms
from ..datahelper.students.studentsDataAdd import *
from ..datahelper.students.studentsDataDelete import *

# --- CREDIT PLANNER ---
class MajorForm(forms.Form):
    major = forms.CharField(label='major', required=True) 
    def process(self, request, add_or_delete='add'):
        major = self.cleaned_data.get('major')
        if add_or_delete == 'add':
            addMajor(request, major)
        if add_or_delete == 'delete':
            deleteMajor(request, major)


class YearForm(forms.Form):
    year = forms.CharField(label='year', required=True) 
    def process(self, request, add_or_delete='add'):
        year = self.cleaned_data.get('year')
        if add_or_delete == 'add':
            addYear(request, year)
        if add_or_delete == 'delete':
            deleteYear(request, year)


class SemesterForm(forms.Form):
    year = forms.CharField(label='year', required=True) 
    semester = forms.CharField(label='semester', required=True) 
    def process(self, request, add_or_delete='add'):
        year = self.cleaned_data.get('year')
        semester = self.cleaned_data.get('semester')
        if add_or_delete == 'add':
            addSemester(request, year, semester)
        if add_or_delete == 'delete':
            deleteSemester(request, year, semester)

    class Meta:
        model = Semester
        exclude = ['pk',]


class CourseForm(forms.Form):
    year = forms.CharField(label='years', required=True)
    semester = forms.CharField(label='semester', required=True)
    course = forms.CharField(label='course', required=True) 
    def process(self, request, add_or_delete='add'):
        year = self.cleaned_data.get('year')
        semester = self.cleaned_data.get('semester')
        course = self.cleaned_data.get('course')
        if add_or_delete == 'add':
            addCourse(request, year, semester, course)
        if add_or_delete == 'delete':
            deleteCourse(request, year, semester, course)

class APForm(forms.Form):
    test_name = forms.CharField(label='test_name', required=True)
    score = forms.CharField(label='score', required=True) 
    def process(self, request, add_or_delete='add'):
        test_name = self.cleaned_data.get('test_name')
        score = self.cleaned_data.get('score')
        if add_or_delete == 'add':
            addAP(request, test_name, score)
        if add_or_delete == 'delete':
            deleteAP(request, test_name, score) 


