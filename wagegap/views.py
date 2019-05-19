from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
from .models import *

def index(request):
    countries = []
    for country in Country.objects.all():
        countries.append(country)

    if (request.GET.get('wagesubmit')):
        try:
            wage = int(request.GET.get('wagebox'))
            country_name= request.GET.get('country_name')
            return redirect('purchase-power', country_name=country_name, wage=wage)
        except TypeError:
             print("Wrong input")


    context = {
         'countries': countries
     }
    return render(request, 'wagegap/index.html', context)

def purchase_power(request, country_name, wage):
    country = Country.objects.get(name=country_name)
    '''dict od dicts
    {category: {spending: price}}'''
    current_numbers = dict()

    for category in Category.objects.all():
        current_numbers[category.name] = dict()

    for item in Cost.objects.all().filter(country=country):
        price = item.price
        spending = item.spending
        category = spending.category
        current_numbers[category.name][spending.name] = price

    context = {
         'current_numbers': current_numbers.items,
     }
    return render(request, 'wagegap/purchase_power.html', context)
