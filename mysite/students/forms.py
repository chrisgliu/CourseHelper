from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.core.mail import EmailMessage  
from .models import Student, Enrolled, Major, Year, Semester, Course
from django.forms import ModelForm

# --- SIGN UP --- 
class SignUpForm(UserCreationForm):  

    def saveButDontActivate(self):
        user = self.save(commit=False)  
        user.is_active = False  
        username = self.cleaned_data.get('username')  
        firstname = self.cleaned_data.get('first_name')  
        lastname = self.cleaned_data.get('last_name')  
        newstudent = Student(firstname=firstname, lastname=lastname, username=username)
        newstudent.save()
        enroll = Enrolled(enrolled = True)
        enroll.students = newstudent
        enroll.save()
        user.save() 
        return user

    def sendActivationEmail(self, request, user):
        current_site = get_current_site(request) 
        mail_subject = 'Activate your account.'  
        message = render_to_string('students/acc_active_email.html', {  
            'user': user,  
            'domain': current_site.domain,  
            'uid':  urlsafe_base64_encode(force_bytes(user.pk)),  
            'token': account_activation_token.make_token(user),  
        })  
        to_email = self.cleaned_data.get('email')  
        email = EmailMessage( mail_subject, message, to=[to_email] )  
        email.send()

    class Meta:  
        model = User  
        fields = ('email', 'first_name', 'last_name', 'username')

# --- CREDIT PLANNER --- 
class AddMajor(ModelForm):
    def process(self, user):
        major = self.cleaned_data.get('major')  
        selection = Major(major=major)
        firstname = user.first_name
        lastname = user.last_name
        username = user.username
        student = Student.objects.filter(firstname=firstname, lastname=lastname, username=username).first()
        enrollment = Enrolled.objects.filter(students=student).first()
        selection.save()
        selection.enrolled.add(enrollment)
        selection.save()
    class Meta:
        model = Major
        fields = ['major']
# --- CLASS SCHEDULE --- 
class AddYear(ModelForm):
    def process(self, user):
        year = self.cleaned_data.get('year')  
        selection = Year(year=year)
        firstname = user.first_name
        lastname = user.last_name
        username = user.username
        student = Student.objects.filter(firstname=firstname, lastname=lastname, username=username).first()
        enrollment = Enrolled.objects.filter(students=student).first()
        selection.save()
        selection.enrolled.add(enrollment)
        selection.save()
    class Meta:
        model =Year
        fields = ['year']

class AddSemester(ModelForm):
    def process(self, user, theyear):
        semester = self.cleaned_data.get('semester')  
        selection = Semester(semester=semester)
        firstname = user.first_name
        lastname = user.last_name
        username = user.username
        student = Student.objects.filter(firstname=firstname, lastname=lastname, username=username).first()
        enrollment = Enrolled.objects.filter(students=student).first()
        year = Year.objects.filter(enrolled=enrollment, year=theyear)
        selection.save()
        selection.years.add(year)
        selection.save()
    class Meta:
        model = Semester
        fields = ['semester']

class AddCourse(ModelForm):
    def process(self, user, theyear, thesemester):
        course = self.cleaned_data.get('course')  
        selection = Course(course=course)
        firstname = user.first_name
        lastname = user.last_name
        username = user.username
        student = Student.objects.filter(firstname=firstname, lastname=lastname, username=username).first()
        enrollment = Enrolled.objects.filter(students=student).first()
        year = Year.objects.filter(enrolled=enrollment, year=theyear)
        semester = Semester.objects.filter(years=year, semester=thesemester)
        selection.save()
        selection.semesters.add(semester)
        selection.save()
    class Meta:
        model = Course
        fields = ['course']



# --- BUDGET TRACKER ---

