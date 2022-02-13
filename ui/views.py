from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import json
import requests

def index(request):
    response = requests.get("http://api.coincap.io/v2/assets").text
    data = json.loads(response)
    content = []
    for coin in data['data']:
        content.append([coin['rank'], coin['symbol'], coin['name'], coin['priceUsd']])
    template = loader.get_template('ui/index.html')
    return HttpResponse(template.render({'content': content}, request))