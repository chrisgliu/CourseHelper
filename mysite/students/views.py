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

def index(request):
    if not request.user.is_authenticated:
        context = {
            "user": None,
            "links": [["signup", reverse("signup")],["signin", reverse("signin")]]
        }
        return render(request = request, template_name = "students/home.html", context=context)	
    if request.user.is_authenticated:
        context = {
            "user": request.user,
            "links": [["signout", reverse("signout")],]
        }
        return render(request = request, template_name = "students/home.html", context=context)	

def test(request):
    return render(request = request, template_name = "students/newsignup.html")

# when accessed with get, this renders the sign up page with no message
# when accessed with post, registering data is retrieved from the form
# SignUpForm inherits restrictions from UserCreationForm such as password length


def signup(request):
    if request.method == 'GET':  
        return render(request, 'students/newsignup.html', {"message": None, "form.errors": None})  
    if request.method == 'POST':
        form = SignUpForm(request.POST)  
        if form.is_valid():  
            user = form.saveButDontActivate()
            form.sendActivationEmail(request, user)
            message = 'Please confirm your email address to complete the registration'
            return render(request, 'students/newsignup.html', {"message": message, "form.errors": None})    
        else:  
            message = "The operation could not be performed because one or more error(s) occurred."
            return render(request, 'students/newsignup.html', {"message": message, "form": form})  
    
# this is accessed with activation link sent from a confirmation email
# this takes the data from the link and checks if there is a matching use
# if a user is found, the user is then activated
def activate(request, uidb64, token):  
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(id=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')

# when accessed with get, this renders the sign in page with no message
# when accessed with post, login data is retrieved from the form
# if the login data is linked to a valid user, the user is redirected to the main/index page
# else the user is sent back to the sign in page with the message "Invalid credentials."
def signin(request):
    if request.method == "GET":
        return render(request, "students/newsignin.html", {"message": None})
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "students/newsignin.html", {"message": "Invalid credentials."})

# this makes a logout request and renders the sign in page with the message "Logged out."
def signout(request):
    logout(request)
    return render(request, "students/newsignin.html", {"message": "Logged out."})