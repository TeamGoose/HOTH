from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def index (request):
	return HttpResponse('<h1> Sell </h1>')

def getSale (request):
	if request.method == 'POST':
		form = SellForm(request.post)
		if form.is_valid():
			#process the data
			itemName = request.POST.get('itemName')
			sellerName = request.POST.get('sellerName')
			description = request.POST.get('description')
			price = request.POST.get('price')
			emailSeller = request.POST.get('emailSeller')
			sellerNumber = request.POST.get('sellerNumber')
			sell_form = sellForm(itemName = itemName, sellerName = sellerName, description = description, price = price, emailSeller = emailSeller, sellerNumber = sellerNumber)
			sell_form.save()
			return HttpResponseRedirect('/')

		else:
			form = SellForm()

		return render(request, 'sell.html', {'form': form})
