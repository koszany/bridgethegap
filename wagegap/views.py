from django.shortcuts import render, redirect
import requests
from .models import MinWage, CustomWage


def index(request):
    wage = MinWage("Poland")

    if (request.GET.get('wagesubmit')):
        try:
            wage = CustomWage(int(request.GET.get('wagebox')), "Poland", MinWage("Poland"))
        except TypeError:
            print("Wrong input")
        return redirect('purchase-power')

    context = {
        'current_numbers': wage.costs.items,
    }
    print(wage.costs)
    return render(request, 'wagegap/index.html', context)

def purchase_power(request):
    wage = MinWage("France")

    if (request.GET.get('wagesubmit')):
        try:
            wage = CustomWage(int(request.GET.get('wagebox')), "France", MinWage("France"))
        except TypeError:
            print("Wrong input")

    context = {
        'current_numbers': wage.costs,
    }
    return render(request, 'wagegap/purchase_power.html', context)
