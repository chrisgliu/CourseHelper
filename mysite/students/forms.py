from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.forms import ModelForm
from django import forms
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from .studentsdata import *


# --- SIGN UP ---
class SignUpForm(UserCreationForm):

    def saveButDontActivate(self):
        user = self.save(commit=False)
        user.is_active = False
        username = self.cleaned_data.get('username')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        addStudent(first_name, last_name, username)
        this_student = getStudentID(user)
        addEnrollment(this_student)
        user.save()
        return user  # for activation

    def sendActivationEmail(self, request, user):
        current_site = get_current_site(request)
        mail_subject = 'Activate your account.'
        message = render_to_string('students/acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = self.cleaned_data.get('email')
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username')


# --- CREDIT PLANNER ---
class MajorForm(ModelForm):
    def process(self, user, add_or_delete="add"):
        major = self.cleaned_data.get('major')
        if add_or_delete == "add":
            addMajor(user, major)
        if add_or_delete == "delete":
            deleteMajor(user, major)

    class Meta:
        model = Major
        fields = ['major']


class YearForm(ModelForm):
    def process(self, user, add_or_delete="add"):
        year = self.cleaned_data.get('year')
        if add_or_delete == "add":
            addYear(user, year)
        if add_or_delete == "delete":
            deleteYear(user, year)

    class Meta:
        model = Year
        fields = ['year']


class SemesterForm(ModelForm):
    year = forms.CharField(label='years', required=True)

    def process(self, user, add_or_delete="add"):
        year = self.data.get('year')
        semester = self.cleaned_data.get('semester')
        if add_or_delete == "add":
            addSemester(user, year, semester)
        if add_or_delete == "delete":
            deleteSemester(user, year, semester)

    class Meta:
        model = Semester
        fields = ['semester', 'years']


class CourseForm(ModelForm):
    year = forms.CharField(label='years', required=True)
    semester = forms.CharField(label='years', required=True)

    def process(self, user, add_or_delete="add"):
        year = self.data.get('year')
        semester = self.data.get('semester')
        course = self.cleaned_data.get('course')
        if add_or_delete == "add":
            addCourse(user, year, semester, course)
        if add_or_delete == "delete":
            deleteCourse(user, year, semester, course)

    class Meta:
        model = Course
        fields = ['year', 'semester', 'course']

# --- CLASS SCHEDULE ---
# --- BUDGET TRACKER ---
