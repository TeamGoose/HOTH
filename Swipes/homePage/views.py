from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Swipe Me In! or any other working title </h1>")
