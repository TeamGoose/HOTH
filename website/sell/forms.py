from django import forms

class SellForm(forms.Form):
	itemName = form.CharField(max_length = 50)
	sellerName = form.CharField(max_length = 50)
	description = form.CharField(max_length = 100) 
	price = form.DecimalField(max_length = 10, decimal_places = 2)
	emailSeller = form.CharField(max_length = 100)
	sellerNumber = form.IntegerField(max_length = 50)
