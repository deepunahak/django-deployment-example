from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    idx_dict = {'home': 'Apllication connected!!'}
    return(request, "basic_app/index.html", idx_dict)

