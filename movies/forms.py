from django import forms


class Tickets(forms.Form):
    name = forms.CharField(required=True, max_length=35, label='Attendant (Your Name)')
    num_of_sits = forms.IntegerField(required=True, label='Number of sits')

# Form incharge of booking sites in the bank.....
