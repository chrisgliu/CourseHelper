from .viewPages.authPages import *
from .viewPages.budgetPages import *
from .viewPages.creditPages import *
from .viewPages.homePages import *
from .viewPages.schedulePages import *
from django.views.decorators.csrf import csrf_protect

# Create your views here.

@csrf_protect






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



