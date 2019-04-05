from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.http import HttpRequest
from urllib.request import urlopen
import json
import ssl
import re
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import WageForm

from bs4 import BeautifulSoup
from django.template import Template, Context

# This restores the same behavior as before.

def index(request):
    url = 'https://www.numbeo.com/cost-of-living/country_result.jsp?country=Poland'
    context = ssl._create_unverified_context()
    serialized_data = urlopen(url, context=context)

    living_costs = {}
    test = []
    soup = BeautifulSoup(serialized_data, features="html.parser")
    data = soup.get_text().replace('\xa0', ' ').split("\n")

    for item in data:
        if "zł" in str(item):
            item = item.strip().split("  ")
            living_costs[item[0]] = float(item[-1][:-2].strip().replace(',', ''))

    template = loader.get_template('polls/index.html')
    context = {
        'current_numbers': living_costs.items,
    }
    return HttpResponse(template.render(context, request))

def get_wage(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WageForm(request.POST)
        print(form.fields['your_wage'])
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WageForm()


    return render(request, 'index.html', {'form': form})

# Create your views here.
