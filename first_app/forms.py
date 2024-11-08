
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

def validate_bd_phone_number(value):
    if len(value) != 11:
        raise ValidationError("The phone number must be 11 digits long.")
    
    if not value.isdigit():
        raise ValidationError("The phone mumber must contain only numbers.")

class MusicianForm(forms.Form):  
    field = forms.CharField(validators=[validate_bd_phone_number], widget=forms.TextInput(attrs={
        "class": "input input-bordered input-secondary w-full max-w-xs"
    }))














 # firstname = forms.CharField(label="First Name", widget=forms.TextInput(attrs={
    #     "placeholder": "Enter your firstname",
    #     "class": "input input-bordered input-primary w-full"
    # }))

    # lastname = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={
    #     "placeholder": "Enter your lastname",
    #     "class": "input input-bordered input-primary w-full"
    # }))

    # date_of_birth = forms.DateField(label="Date of birth", widget=forms.TextInput(attrs={
    #     "class": "input input-bordered input-primary w-full",
    #     "type": "date"
    # }))

    # instrument = forms.CharField(label="Instrument", widget=forms.TextInput(attrs={
    #     "placeholder": "Enter your firstname",
    #     "class": "input input-bordered input-primary w-full"
    # }))

    # field = forms.BooleanField(required=False)
    # field = forms.CharField(max_length=15, min_length=5)
    # fruits = [
    #     ("", "---SELECT Fruit---"),
    #     ("Apple", "Apple"),
    #     ("Banana", "Banana"),
    #     ("Mango", "Mango"),
    #     ("Orange", "Orange"),
    #     ("Cherry", "Cherry")
    # ]
    # field = forms.ChoiceField(choices=fruits, initial="Mango", widget=forms.Select(attrs={
    #     "class": "select select-bordered",
    # }))

    # OPTIONS = [
    #     ('1', 'Option 1'),
    #     ('2', 'Option 2'),
    #     ('3', 'Option 3')
    # ]
    # field = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect)

