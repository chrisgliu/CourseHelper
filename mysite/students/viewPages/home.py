from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# --- HOME PAGES ---
# home menu reflects if the user is logged in or not

# -- HOME MENU LINKS --
def getLoggedInNav(request):
    return {'signout':True, 'signin':False, 'signup':False, 'name': request.user.first_name}

def getLoggedOutNav():
    return {'signout':False, 'signin':True, 'signup':True}
 
   
# --- HOME PAGES ---
def mergeDict(x, y):
    z = x.copy()
    z.update(y)
    return z


def renderHome(request, template_path, more_context={}):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            loggedOutContext = mergeDict(getLoggedOutNav(), more_context)
            return render(request=request, template_name=template_path, context=loggedOutContext)
        if request.user.is_authenticated:
            loggedInContext = mergeDict(getLoggedInNav(request), more_context)
            return render(request=request, template_name=template_path, context=loggedInContext)
