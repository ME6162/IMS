from django.shortcuts import render

# Create your views here.
import datetime
# Create your views here.
from django.http import HttpResponse


def index(request, institute='Manage'):
    now = datetime.datetime.now()
    #db call to check sc exist
    html = "<html><body><h3>Now time is</h3>" \
           "<h1>Varsha Darling</h1>" \
           "<h1>%s</h1>" \
           "</body></html>" % institute
    return HttpResponse(html)    # rendering the template in HttpResponse


def register(request, institute='Manage'):
    now = datetime.datetime.now()
    html = "<html><body><h1>Register</h1>" \
           "<h1>%s</h1>" \
           "</body></html>" % institute
    return HttpResponse(html)    # rendering the template in HttpResponse
