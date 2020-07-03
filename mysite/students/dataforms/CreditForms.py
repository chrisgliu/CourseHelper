from django.forms import ModelForm
from django import forms
from ..datahelper.students.studentsDataAdd import *
from ..datahelper.students.studentsDataDelete import *

# --- CREDIT PLANNER ---
class MajorForm(ModelForm):
    def process(self, user, add_or_delete='add'):
        major = self.cleaned_data.get('major')
        if add_or_delete == 'add':
            addMajor(user, major)
        if add_or_delete == 'delete':
            deleteMajor(user, major)

    class Meta:
        model = Major
        fields = ['major']


class YearForm(ModelForm):
    def process(self, user, add_or_delete='add'):
        year = self.cleaned_data.get('year')
        if add_or_delete == 'add':
            addYear(user, year)
        if add_or_delete == 'delete':
            deleteYear(user, year)

    class Meta:
        model = Year
        fields = ['year']


class SemesterForm(ModelForm):
    year = forms.CharField(label='years', required=True)

    def process(self, user, add_or_delete='add'):
        year = self.data.get('year')
        semester = self.cleaned_data.get('semester')
        if add_or_delete == 'add':
            addSemester(user, year, semester)
        if add_or_delete == 'delete':
            deleteSemester(user, year, semester)

    class Meta:
        model = Semester
        fields = ['semester', 'years']


class CourseForm(ModelForm):
    year = forms.CharField(label='years', required=True)
    semester = forms.CharField(label='years', required=True)

    def process(self, user, add_or_delete='add'):
        year = self.data.get('year')
        semester = self.data.get('semester')
        course = self.cleaned_data.get('course')
        if add_or_delete == 'add':
            addCourse(user, year, semester, course)
        if add_or_delete == 'delete':
            deleteCourse(user, year, semester, course)

    class Meta:
        model = Course
        fields = ['year', 'semester', 'course']
