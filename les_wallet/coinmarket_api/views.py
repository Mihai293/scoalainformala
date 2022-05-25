import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def coin(request):
    apidata = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    return render(request, 'main.html', {'apidata': apidata})
