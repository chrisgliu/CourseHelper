from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
         return render(request = request,
                template_name = "students/home.html")
    context = {
        "user": request.user
    }
    return render(request, "students/user.html", context)	

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request = request,
                  template_name = "students/signup.html",
                  context={"form":form})
    if request.method == "GET":
        form = UserCreationForm
        return render(request = request,
                template_name = "students/signup.html",
                context={"form":form})

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "students/signin.html", {"message": "Invalid credentials."})
    else:
        return render(request, "students/signin.html", {"message": None})

def signout(request):
    logout(request)
    return render(request, "students/signin.html", {"message": "Logged out."})