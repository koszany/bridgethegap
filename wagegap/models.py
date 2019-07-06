from django.db import models
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MinWage(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    wage = models.IntegerField()
    last_update = models.DateField()

    def __str__(self):
        return 'Minimum wage in {}: {}'.format(str(self.country), str(self.wage))

class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Spending(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return self.name

class Cost(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    spending = models.ForeignKey(Spending, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return '{} costs {} in {}'.format(self.spending, self.price, self.country)
        
