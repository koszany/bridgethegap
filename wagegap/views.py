from django.shortcuts import render
import requests
from .models import MinWage, CustomWage


def index(request):
    wage = MinWage("Poland")

    if (request.GET.get('wagesubmit')):
        try:
            wage = CustomWage(int(request.GET.get('wagebox')), "Poland", MinWage("Poland"))
        except TypeError:
            print("Wrong input")

    context = {
        'current_numbers': wage.costs.items,
    }
    return render(request, 'wagegap/index.html', context)
