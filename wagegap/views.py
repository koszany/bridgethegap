from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import requests
from django.http import HttpRequest
from django.template import loader
from django.http import HttpResponseRedirect
#from .forms import WageForm
from django.template import Template, Context
from .models import MinWage, CustomWage
from django import forms

from django.http import HttpResponseRedirect

# This restores the same behavior as before.

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

def index(request):
    min_wage = MinWage()
    template = loader.get_template('wagegap/index.html')
    context = {
        'current_numbers': min_wage.costs.items,
    }
    return HttpResponse(template.render(context, request))


def send_message(name, message):
    pass
    # Code for actually sending the message goes here


def contact_view(request):
    # The request method 'POST' indicates
    # that the form was submitted
    if request.method == 'POST':  # 1
        # Create a form instance with the submitted data
        form = ContactForm(request.POST)  # 2
        # Validate the form
        if form.is_valid():  # 3
            # If the form is valid, perform some kind of
            # operation, for example sending a message
            send_message(
                form.cleaned_data['name'],
                form.cleaned_data['message']
            )
            # After the operation was successful,
            # redirect to some other page
            return redirect('/success/')  # 4
    else:  # 5
        # Create an empty form instance
        form = ContactForm()

    return render(request, 'your_wage.html', {'form': form})

class WageForm(forms.Form):
    your_wage = forms.CharField(label='Your monthly wage in PLN: ', max_length=100)


def scale_living_costs(request):
    # if this is a POST request we need to process the form data
    custom_wage = CustomWage(5000)
    template = loader.get_template('wagegap/your-wage.html')
    context = {
        'current_numbers': custom_wage.costs.items,
    }
    return HttpResponseRedirect(template.render(context, request))

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


    return render(request, 'your-wage.html', {'form': form})

# Create your views here.
