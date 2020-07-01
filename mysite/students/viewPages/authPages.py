from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from ..tokens import account_activation_token
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from ..dataforms.SignUpForm import SignUpForm

# --- SIGN UP ---
def signUpPage(request):
    if request.method == 'GET':
        return render(request, 'students/signUp.html')


def signUpForm(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.saveButDontActivate()
            form.sendActivationEmail(request, user)
            message = 'Please confirm your email address to complete the registration'
            return render(request, 'students/signUp.html', {"message": message})
        else:
            message = "The operation could not be performed because one or more error(s) occurred"
            return render(request, 'students/signUp.html', {"message": message, "form": form})
    message = 'Please enter information here'
    return render(request, "students/signUp.html", {"message": message})


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
        return render(request, 'students/signUp.html', {"message": message})

# --- SIGN IN ---
def signInPage(request):
    if request.method == "GET":
        return render(request, "students/signIn.html")

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
