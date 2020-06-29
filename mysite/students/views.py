from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from .forms import SignUpForm, MajorForm, YearForm, SemesterForm, CourseForm
from .coursesdata import *
from .studentsdata import *


# Create your views here.

# --- TESTING --- 
def test(request):
    data = getMajorsList(request)
    return HttpResponse(data)


# --- NOTES ---
# -- pages --
# home menu reflects if the user is logged in or not
# home bar reflects if the user is on the credit, sched, or budget page
# -- forms --
# process html forms that manipulate the models
# -- models --
# access data from models

# -- HOME MENU LINKS --
def getLoggedInLinks(request):
    return {"links": [["Sign out", reverse("signOut")]], "name": request.user.first_name}


def getLoggedOutLinks():
    return {"links": [["Sign up", reverse("signUp")], ["Sign in", reverse("signIn")]]}


# -- DISPLAY MODELS --


# --- ABOUT ---
def aboutPage(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request=request, template_name="students/about.html", context=getLoggedOutLinks())
        if request.user.is_authenticated:
            return render(request=request, template_name="students/about.html", context=getLoggedInLinks(request))


# --- CREDIT PLANNER ---
def creditPage(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request=request, template_name="students/credit.html", context=getLoggedOutLinks())
        if request.user.is_authenticated:
            return render(request=request, template_name="students/credit.html", context=getLoggedInLinks(request))


def creditForm(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = MajorForm(request.POST)
            if form.is_valid():
                form.process(request.user)
                return HttpResponseRedirect(reverse("credit"))
    return render(request, "students/signIn.html", {"message": "Sign in first"})


# --- CLASS SCHEDULE --- 
def schedulePage(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request=request, template_name="students/schedule.html", context=getLoggedOutLinks())
        if request.user.is_authenticated:
            return render(request=request, template_name="students/schedule.html", context=getLoggedInLinks(request))


def scheduleForm(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = MajorForm(request.POST)
            if form.is_valid():
                form.process(request.user)
                return HttpResponseRedirect(reverse("schedule"))
    return render(request, "students/signIn.html", {"message": "Sign in first"})


# --- BUDGET TRACKER ---
def budgetPage(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request=request, template_name="students/budget.html", context=getLoggedOutLinks())
        if request.user.is_authenticated:
            return render(request=request, template_name="students/budget.html", context=getLoggedInLinks(request))


def budgetForm(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = MajorForm(request.POST)
            if form.is_valid():
                form.process(request.user)
                return HttpResponseRedirect(reverse("schedule"))
    return render(request, "students/signIn.html", {"message": "Sign in first"})


# --- SIGN UP ---
def signUpPage(request):
    if request.method == 'GET':
        return render(request, 'students/signUp.html', {"message": None, "form.errors": None})


def signUpForm(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.saveButDontActivate()
            form.sendActivationEmail(request, user)
            message = 'Please confirm your email address to complete the registration'
            return render(request, 'students/signUp.html', {"message": message, "form": None})
        else:
            message = "The operation could not be performed because one or more error(s) occurred."
            return render(request, 'students/signUp.html', {"message": message, "form": form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        message = 'Thank you for your email confirmation. Now you can login your account.'
        return render(request, "students/signIn.html", {"message": message})
    else:
        message = 'Activation link is invalid!'
        return render(request, 'students/signUp.html', {"message": message, "form": None})

    # --- SIGN IN ---


def signInPage(request):
    if request.method == "GET":
        return render(request, "students/signIn.html", {"message": None})


def signInForm(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("credit"))
        else:
            return render(request, "students/signIn.html", {"message": "Invalid credentials."})


def signOut(request):
    logout(request)
    return render(request, "students/signIn.html", {"message": "Logged out."})
