import requests

from django.shortcuts import render
from django.conf import settings


def get_cryptocurrency(request):
    apidata = requests.get(settings.PARSE_URL).json()
    return render(request, 'index.html', context={'apidata': apidata})
