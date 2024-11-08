from django.shortcuts import render
from first_app.models import Musician, Album
from first_app import forms

# Create your views here.

def home(request):
    return render(request, 'first_app/home.html')

def displayMusicians(request):
    musicians = Musician.objects.values()
    return render(request, 'first_app/musicians.html', context={"musicians": musicians})

def form(request):
    return render(request, 'first_app/form.html', context={})

def django_form(request):

    musician_form = forms.MusicianForm()
    diction = {"musicianForm": musician_form}

    if request.method == "POST":
        musician_form= forms.MusicianForm(request.POST)

        if musician_form.is_valid():
            diction.update({"field": musician_form.cleaned_data["field"], "musicianForm": musician_form})

        else:
            diction.update({"musicianForm": musician_form})
        # if musician_form.is_valid():
        #     first_name = musician_form.cleaned_data['firstname']
        #     last_name = musician_form.cleaned_data['lastname']
        #     instrument = musician_form.cleaned_data['instrument']

        #     return render(request, 'first_app/djangoform.html', context={"musicianForm": musician_form, "data": {
        #         "first_name": first_name,
        #         "last_name": last_name,
        #         "instrument": instrument
        #     }})


    return render(request, 'first_app/djangoform.html', context=diction)
