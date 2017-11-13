from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
import sys


def index (request):
    try:
        sys.path.insert(0, "../sell")
        from sell.models import sellEntry
        dbList = sellEntry.objects.all()#order_by('id')
        context = {'dbList': dbList}
        return render(request, 'index.html', context)
        #return HttpResponse('<h1> Bruin List </h1>')
    except ImportError:
        print('No Import')
        return HttpResponse('<h1> No imports! </h1>')
