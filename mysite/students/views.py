from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse
from .forms import SignUpForm
from django.contrib.auth.models import User  
from django.utils.encoding import force_bytes, force_text 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from .tokens import account_activation_token  

# Create your views here.

def getloggedinlinks(request):
    return { "links": [["Sign out", reverse("signout")]], "name": request.user.first_name }
def getloggedoutinks():
    return  { "links": [["Sign up", reverse("signup")],["Sign in", reverse("signin")]] }

# main page
# the homebar reflects if the user is logged in or not
def index(request):
    if not request.user.is_authenticated:
        return render(request = request, template_name = "students/home.html", context=getloggedoutinks())	
    if request.user.is_authenticated:
        return render(request = request, template_name = "students/home.html", context=getloggedinlinks(request))	

# testing
def test(request):
    return render(request = request, template_name = "students/home.html")

# when accessed with get, this renders the sign up page with no message
# when accessed with post, registering data is retrieved from the form
# SignUpForm inherits restrictions from UserCreationForm such as password length
# When errors are caught with UserCreationForm, a list of errors is rendered
def signup(request):
    if request.method == 'GET':  
        return render(request, 'students/signup.html', {"message": None, "form.errors": None})  
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
    
# this is accessed with activation link sent from a confirmation email
# this takes the data from the link and checks if there is a matching user
# if a user is found, the user is then activated and the sign in page is rendered
# else the sign up page is rendered
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

# when accessed with get, this renders the sign in page with no message
# when accessed with post, login data is retrieved from the form
# if the login data is linked to a valid user, the user is redirected to the main/index page
# else the user is sent back to the sign in page with the message "Invalid credentials."
def signin(request):
    if request.method == "GET":
        return render(request, "students/signin.html", {"message": None})
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "students/signin.html", {"message": "Invalid credentials."})

# this makes a logout request and renders the sign in page with the message "Logged out."
def signout(request):
    logout(request)
    return render(request, "students/signin.html", {"message": "Logged out."})

# the homebar reflects if the user is logged in or not
# about page
def about(request):
    if not request.user.is_authenticated:
        return render(request = request, template_name = "students/about.html", context=getloggedoutinks())	
    if request.user.is_authenticated:
        return render(request = request, template_name = "students/about.html", context=getloggedinlinks(request))