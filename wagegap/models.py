from django.db import models
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

# Create your models here.
class MinWage:

    def __init__(self, country="Poland"):
        self.COUNTRY = country
        self.CURRENCY = "PLN"
        self.URL_DATA = 'https://www.numbeo.com/cost-of-living/country_result.jsp?country=Poland'
        self.MINIMAL_WAGE = 1634
        self.load_prices()


    def load_prices(self):
        self.costs = {}
        context = ssl._create_unverified_context()
        serialized_data = urlopen(self.URL_DATA, context=context)

        soup = BeautifulSoup(serialized_data, features="html.parser")
        data = soup.get_text().replace('\xa0', ' ').split("\n")

        for item in data:
            if "zł" in str(item):
                item = item.strip().split("  ")
                self.costs[item[0]] = float(item[-1][:-2].strip().replace(',', ''))

class CustomWage:

    def __init__(self, wage, country="Poland"):
        self.min_wage = MinWage(country)
        self.wage = wage
        self.rescale_prices()

    def rescale_prices(self):
        self.costs = {}
        scale_factor = self.wage/self.MinWage
        for item, real_cost in self.min_wage.costs.items():
            self.costs[item] = real_cost * scale_factor
