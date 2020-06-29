from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse
from django.contrib.auth.models import User  
from django.utils.encoding import force_bytes, force_text 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from .tokens import account_activation_token  
from .models import Student, Enrolled, Major, Year, Semester, Course
from .forms import SignUpForm, AddMajor

# Create your views here.

# --- TESTING --- 
def test(request):
    return render(request = request, template_name = "students/home.html")

# --- NOTES --- 
# -- pages --
# home menu reflects if the user is logged in or not
# home bar reflects if the user is on the credit, sched, or budget page
# -- forms --
# process html forms that manipulate the models
# -- models --
# access data from models

# -- HOME MENU LINKS --
def getloggedinlinks(request):
    return { "links": [["Sign out", reverse("signout")]], "name": request.user.first_name }
def getloggedoutinks():
    return  { "links": [["Sign up", reverse("signup")],["Sign in", reverse("signin")]] }
# -- DISPLAY MODELS --



# --- ABOUT --- 
def aboutpage(request):
    if request.method == 'GET': 
        if not request.user.is_authenticated:
            return render(request = request, template_name = "students/about.html", context=getloggedoutinks())	
        if request.user.is_authenticated:
            return render(request = request, template_name = "students/about.html", context=getloggedinlinks(request))

# --- CREDIT PLANNER --- 
def creditpage(request):
    if request.method == 'GET': 
        if not request.user.is_authenticated:
            return render(request = request, template_name = "students/credit.html", context=getloggedoutinks())	
        if request.user.is_authenticated:
            return render(request = request, template_name = "students/credit.html", context=getloggedinlinks(request))

def creditform(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = AddMajor(request.POST)  
            if form.is_valid():  
                form.process(request.user)
                return HttpResponseRedirect(reverse("credit"))
    return render(request, "students/signin.html", {"message": "Sign in first"})
    
# --- CLASS SCHEDULE --- 
def schedpage(request):
    if request.method == 'GET': 
        if not request.user.is_authenticated:
            return render(request = request, template_name = "students/sched.html", context=getloggedoutinks())	
        if request.user.is_authenticated:
            return render(request = request, template_name = "students/sched.html", context=getloggedinlinks(request))

def schedform(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = AddMajor(request.POST)  
            if form.is_valid():  
                form.process(request.user)
                return HttpResponseRedirect(reverse("sched"))
    return render(request, "students/signin.html", {"message": "Sign in first"})

# --- BUDGET TRACKER ---  
def budgetpage(request):
    if request.method == 'GET': 
        if not request.user.is_authenticated:
            return render(request = request, template_name = "students/budget.html", context=getloggedoutinks())	
        if request.user.is_authenticated:
            return render(request = request, template_name = "students/budget.html", context=getloggedinlinks(request))

def budgetform(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = AddMajor(request.POST)  
            if form.is_valid():  
                form.process(request.user)
                return HttpResponseRedirect(reverse("sched"))
    return render(request, "students/signin.html", {"message": "Sign in first"})

# --- SIGN UP --- 
def signuppage(request):
    if request.method == 'GET':  
        return render(request, 'students/signup.html', {"message": None, "form.errors": None})  

def signupform(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)  
        if form.is_valid():  
            user = form.saveButDontActivate()
            form.sendActivationEmail(request, user)
            message = 'Please confirm your email address to complete the registration'
            return render(request, 'students/signup.html', {"message": message, "form": None})    
        else:  
            message = "The operation could not be performed because one or more error(s) occurred."
            return render(request, 'students/signup.html', {"message": message, "form": form})  

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
        return render(request, "students/signin.html", {"message": message})  
    else:  
        message = 'Activation link is invalid!'
        return render(request, 'students/signup.html', {"message": message, "form": None}) 

# --- SIGN IN --- 
def signinpage(request):
    if request.method == "GET":
        return render(request, "students/signin.html", {"message": None})

def signinform(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("credit"))
        else:
            return render(request, "students/signin.html", {"message": "Invalid credentials."})

def signout(request):
    logout(request)
    return render(request, "students/signin.html", {"message": "Logged out."})