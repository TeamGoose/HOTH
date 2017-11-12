from django.db import models
import datetime


# Create your models here.

class sellEntry (models.Model):
	itemName = models.CharField(max_length = 50)
	sellerName = models.CharField(max_length = 50)
	description = models.CharField(max_length = 100)
	datePosted = models.CharField(max_length = 50)
	dateAndTimeNow = datetime.datetime.now()
	year = str(dateAndTimeNow.year)
	month = str(dateAndTimeNow.month)
	day = str(dateAndTimeNow.day)
	hour = str(dateAndTimeNow.hour)
	minute = str(dateAndTimeNow.minute)
	dateDB = year + '/' + month + '/' + day + "/" + hour + '/' + minute
	datePosted = dateDB
	locationOfSeller = models.CharField(max_length = 100)
	

