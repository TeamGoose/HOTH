from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from ...sell.models import sellEntry
# Create your views here.
import sys
sys.path.insert(0, "../sell")
try:
    from .models import sellEntry
except ImportError:
    print('No Import')
def index (request):
	   db =1
        #return HttpResponse('<h1> Bruin List </h1>')
