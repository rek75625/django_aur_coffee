from django.db import models
from django.utils import timezone

# Create your models here.
class CoffeeVary(models.Model):
    COFFEE_TYPE_CHOICESN =[("ES","ESPRESSO"),
                           ("LT","LATTE"),
                           ("MH","MACCHIATO"),
                           ("FW","FLAT WHITEZ"),
                           ("CP","CAPPUCCINO"),]


    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='coffees/')
    date_time = models.DateTimeField(default=timezone.now)
    types = models.CharField(max_length=2,choices=COFFEE_TYPE_CHOICESN)