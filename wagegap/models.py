from django.db import models
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

# Create your models here.
class MinWage():

    def __init__(self, country):
        self.COUNTRY = country
        self.URL_DATA = 'https://www.numbeo.com/cost-of-living/country_result.jsp?country='+self.COUNTRY+'&displayCurrency=EUR'
        self.MINIMAL_WAGE = 379
        self.costs = {}
        self.load_prices()


    def load_prices(self):

        context = ssl._create_unverified_context()
        serialized_data = urlopen(self.URL_DATA, context=context)

        soup = BeautifulSoup(serialized_data, features="html.parser")
        data = soup.get_text().replace('\xa0', ' ').split("\n")

        glob_dict = {}
        category='No category'
        for item in data:
            if '[ Edit ]' in item:
                category = item.strip('[ Edit ]')
                self.costs[category] = {}
            if chr(8364) in item:
                item = item.strip().split("  ")
                self.costs[category][item[0]] = float(item[-1][:-2].strip().replace(',', ''))

class CustomWage:

    def __init__(self, wage, country, min_wage):
        self.min_wage = min_wage
        self.wage = wage
        self.costs = {}
        self.rescale_prices()


    def rescale_prices(self):
        scale_factor = self.wage/self.min_wage.MINIMAL_WAGE
        for item, real_cost in self.min_wage.costs.items():
            self.costs[item] = round(real_cost * scale_factor, 2)
