from django.db import models
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl


class Country(models.Model):
    name = models.CharField(max_length=100)

class MinWage(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    wage = models.IntegerField()
    last_update = models.DateField()

class Category(models.Model):
    name = models.TextField()

class Spending(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.TextField()

class Cost(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    spending = models.ForeignKey(Spending, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    last_update = models.DateField(auto_now=True)
