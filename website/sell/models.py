from django.db import models
import datetime

# Create your models here.
class sellEntry (models.Model):
	itemName = models.CharField(max_length = 50, default = "")
	sellerName = models.CharField(max_length = 50, default = "")
	description = models.CharField(max_length = 100, default = "")
	datePosted = models.DateField(auto_now_add=True)
	locationOfSeller = models.CharField(max_length = 100, default = "")
	price = models.DecimalField(max_digits=10, decimal_places=2, default = 0)
	latOfSeller = models.DecimalField(max_digits = 10, decimal_places = 10,default = 0 )
	longOfSeller = models.DecimalField(max_digits = 10, decimal_places = 10, default = 0)
	emailSeller = models.CharField(max_length = 100, default = "")
	sellerNumber = models.IntegerField(max_digits=10, default = 0)