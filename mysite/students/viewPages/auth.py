from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from ..tokens import account_activation_token
from ..dataforms.SignUpForm import SignUpForm
from .home import renderHome
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# --- SIGN UP ---
def signUpFormHelper(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.saveButDontActivate(request)
            form.sendActivationEmail(request, user)
            message = 'Please confirm your email address to complete the registration'
            return renderHome(request, 'students/main.html', more_context={"messages": [message]})
        else:
            message = "The operation could not be performed because one or more error(s) occurred"
            return renderHome(request, 'students/main.html', more_context={"messages": [message], "form": form})
    return HttpResponseRedirect(reverse("main"))

# --- ACTIVATION ---
def activateHelper(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        message = 'Thank you for your email confirmation. Now you can login your account.'
        return renderHome(request, 'students/main.html', {"messages": [message]}) 
    else:
        message = 'Activation link is invalid!'
        return renderHome(request, 'students/main.html', {"messages": [message]}) 

# --- SIGN IN ---
def signInFormHelper(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("main"))
        else:
            message = 'Invalid credentials.'
            return renderHome(request, 'students/main.html', {"messages": [message]}) 

# --- SIGN OUT ---
def signOutHelper(request):
    logout(request)
    message = 'Logged out.'
    return renderHome(request, 'students/main.html', {"messages": [message]}) 
