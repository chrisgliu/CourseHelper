from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# --- HOME PAGES ---
# home menu reflects if the user is logged in or not
# home bar reflects if the user is on the credit, sched, or budget page

# --- TESTING --- 
def test(request):
    return HttpResponse("Helllo World")

# -- HOME MENU LINKS --
def getLoggedInLinks(request):
    return {"links": [["Sign out", reverse("signOut")]], "name": request.user.first_name}


def getLoggedOutLinks():
    return {"links": [["Sign up", reverse("signUp")], ["Sign in", reverse("signIn")]]}

# --- HOME PAGES ---
def mergeDict(x, y):
    z = x.copy()
    z.update(y)
    return z


def renderHome(request, template_path, more_context):
    loggedInContext = mergeDict(getLoggedInLinks(request), more_context)
    loggedOutContext = mergeDict(getLoggedOutLinks(), more_context)
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request=request, template_name="students/about.html", context=loggedInContext)
        if request.user.is_authenticated:
            return render(request=request, template_name="students/about.html", context=loggedOutContext)
