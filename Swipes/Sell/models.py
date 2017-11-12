from django.db import models

# Create your models here.
class SellEntry(models.Model):
    DINING_HALL_CHOICES = (
        ('FST', 'Feast'),
        ('COV', 'Covel'),
        ('DNVE', 'De Neve'),
        ('BPLT', 'Bruin Plate'),
        ('1919', 'Cafe 1919'),
        ('BCAF', 'Bruin Cafe'),
        ('STDY', 'The Study'),
        ('REND', 'Rendevous'),
    )
    dining_hall = models.CharField(
        max_length=4,
        choices=DINING_HALL_CHOICES,
        default='FST',
    )
    comment = models.CharField(max_length=200)
