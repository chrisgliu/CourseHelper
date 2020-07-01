from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from .forms import SignUpForm, MajorForm, YearForm, SemesterForm, CourseForm
from .datahelper.coursesdata import *
from .datahelper.studentsdata import *
from django.views.decorators.csrf import csrf_protect

# Create your views here.







# --- NOTES ---
# -- pages --
# -- forms --
# process html forms that manipulate the models
# -- models --
# access data from models


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

@csrf_protect
def creditMajorFormAdd(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = MajorForm(request.POST)
            if form.is_valid():
                form.process(request.user, 'add')
                return HttpResponseRedirect(reverse("credit"))
    return render(request, "students/signIn.html", {"message": "Sign in first"})


@csrf_protect
def creditMajorFormDelete(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = MajorForm(request.POST)
            if form.is_valid():
                form.process(request.user, 'delete')
                return HttpResponseRedirect(reverse("credit"))
    return render(request, "students/signIn.html", {"message": "Sign in first"})


# --- CLASS SCHEDULE --- 
def schedulePage(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request=request, template_name="students/schedule.html", context=getLoggedOutLinks())
        if request.user.is_authenticated:
            return render(request=request, template_name="students/schedule.html", context=getLoggedInLinks(request))

@csrf_protect
@require_POST
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

@csrf_protect
@require_POST
def budgetForm(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = MajorForm(request.POST)
            if form.is_valid():
                form.process(request.user)
                return HttpResponseRedirect(reverse("schedule"))
    return render(request, "students/signIn.html", {"message": "Sign in first"})



# -- DISPLAY MODELS --


