from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def getSale (request):
	if request.method == 'POST':
		print (" iz post method")
		form = SellForm(request.post)
		if form.is_valid():
			print(":form is vvalid")
			#process the data
			itemName = request.POST.get('itemName')
			sellerName = request.POST.get('sellerName')
			description = request.POST.get('description')
			price = request.POST.get('price')
			emailSeller = request.POST.get('emailSeller')
			sellerNumber = request.POST.get('sellerNumber')
			sell_form = sellForm(itemName = itemName, sellerName = sellerName, description = description, price = price, emailSeller = emailSeller, sellerNumber = sellerNumber)
			sell_form.save()
			print("saved")
			return HttpResponseRedirect('/')

		else:
			form = SellForm()
			print("triggered else")
	return render(request, 'sell.html')
