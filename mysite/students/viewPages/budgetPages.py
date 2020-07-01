from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .homePages import renderHome
from ..dataforms.BudgetForms import *

# --- BUDGET TRACKER ---
def budgetPageHelper(request):
    return renderHome(request, 'students/budget.html')