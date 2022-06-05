import requests
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='rates')
@stringfilter
def rates(symbol, value):
    result = 0
    apidata = requests.get(
        f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    for i in apidata:
        if i['symbol'] == symbol:
            result = float(i['current_price']) * float(value)
            break
    return result
