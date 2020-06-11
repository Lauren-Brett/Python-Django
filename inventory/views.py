from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. - not the views here, the functions here


def index(request):
    return HttpResponse("Hello from the inventory index")