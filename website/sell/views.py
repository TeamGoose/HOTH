from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def index (request):
	return HttpResponse('<h1> Sell </h1>')

def getSale (request):
	if request.method = 'POST':
		form = SellForm(request.post)
		if form.is_valid():
			#process the data


			return HttpResponseRedirect('/')

		else:
			form = SellForm()

		return render(request, 'sell.html', {'form': form})