from django import forms



class WageForm(forms.Form):
    your_wage = forms.CharField(label='Your monthly wage in PLN: ', max_length=100)
