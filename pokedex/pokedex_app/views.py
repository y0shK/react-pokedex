from django.shortcuts import render

import requests

from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

# index.html
def index(request):
    return HttpResponse("Hello world! First view")

# pokeapi test
# https://requests.readthedocs.io/en/latest/user/quickstart/
# https://stackoverflow.com/questions/30259452/proper-way-to-consume-data-from-restful-api-in-django
# https://stackoverflow.com/questions/11663945/calling-a-rest-api-from-django-view

def pokeapi_view(request):
    r = requests.get('https://pokeapi.co/api/v2/pokemon/dewott')
    pkmn_json = r.json()
    # return render(request, 'pkmn_json.html', pkmn_json)
    return JsonResponse(pkmn_json)