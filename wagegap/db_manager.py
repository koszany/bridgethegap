from .models import *
from wagegap.parser import parser

def create_all_spendings_categories():
    for object in Category.objects.all():
        object.delete()

    for object in Spending.objects.all():
        object.delete()

    spending2category = parser.get_spending2category_dict()
    for key, value in spending2category.items():
        category = Category(name=key)
        category.save()
        for item in value:
            Spending(category=category, name=item).save()

def create_all_countries_wages():
    for object in Country.objects.all():
        object.delete()

    for object in MinWage.objects.all():
        object.delete()

    wage2country = parser.get_min_wages()

    for item in wage2country:
        country = Country(name=item[0])
        country.save()
        MinWage(country=country, wage=item[1], last_update=item[2]).save()

def create_all_costs():
    for object in Cost.objects.all():
        object.delete()

    for country in Country.objects.all():
        data = parser.get_price2spending_dict(country.name)
        for k, v in data.items():
            category = Category.objects.get(name=k[0])
            spending = Spending.objects.get(name=k[1], category=category)
            Cost(country=country, spending=spending, price=v).save()

def create_all():
    create_all_spendings_categories()
    create_all_countries_wages()
    create_all_costs()
