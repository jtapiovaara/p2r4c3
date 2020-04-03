import json
import random
import requests
from rest_framework import generics
from .serializers import NatParkSerializer
from django.views import generic
from django.shortcuts import render
from .models import CatTable, NatPark, Seuraaja


class ListNatPark(generics.ListCreateAPIView):
    queryset = NatPark.objects.all()
    serializer_class = NatParkSerializer


class DetailNatPark(generics.RetrieveUpdateDestroyAPIView):
    queryset = NatPark.objects.all()
    serializer_class = NatParkSerializer


class Raportti(generic.ListView):
    model = Seuraaja


def Startaatooseetrii(response):

    # Helsingin ennuste 3 h päähän
    url = 'http://api.openweathermap.org/data/2.5/forecast?id=658225&units=metric&APPID=88b98c1b6cdea2bfed07ed9333ba3790'

    r = requests.get(url.format(658225)).json()

    ennuste = {
        'city': 658225,
        'temp': r['list'][2]['main']['temp'],
        'description': r['list'][2]['weather'][0]['description'],
    }

    # Great Words

    with open('quotes.json', 'r') as f:
        quotes = json.load(f)

        quote = (random.choice(quotes))

    # Random KissaFakta

    cats = CatTable.objects.all()
    randomcat = (random.choice(cats))

    # NatParks

    natparks = NatPark.objects.all()

    # Seuraajat

    # err_msg = ''
    # message = ''
    #
    # fields = [
    #     'maili'
    # ]
    #
    # if request.method == 'POST':
    #     form = Seuraaja(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         message = 'Hieno homma, tervetuloa, tarkista sähköpostisi.'
    #         print(form)
    #     else:
    #         message = err_msg
    # form = Seuraaja()

    curl = 'https://corona.lmao.ninja/countries/Finland'
    # curl = 'https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/finnishCoronaData'

    n = requests.get(curl).json()
    # print(n)

    # vikaalue_act = n['confirmed'][-1]['healthCareDistrict']
    # tapausnro_act = n['confirmed'][-1]['id']
    # menehtyneet = n['deaths'][-1]['id']
    # vikaalue_rec = n['recovered'][-1]['healthCareDistrict']
    # tapausnro_rec = n['recovered'][-1]['id']

    tapausnro_act = n['cases']
    menehtyneet = n['deaths']
    tapausnro_rec = n['recovered']


    context = {
        'ennuste': ennuste,
        'randomcat': randomcat,
        'natparks': natparks,
        'quote': quote,
        'tapausnro_act': tapausnro_act,
        'menehtyneet': menehtyneet,
        'tapausnro_rec': tapausnro_rec,
        # 'message': message,
        # 'form': form,
    }
    return render(response, 'aatooseetrii/aatooseetrii.html', {'context': context})



