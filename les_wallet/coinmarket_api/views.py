from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from coinmarket_api.models import Wallet


@login_required
def coin(request):
    apidata = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    return render(request, 'index.html', {'apidata': apidata})


class WalletView(LoginRequiredMixin, ListView):
    model = Wallet
    template_name = 'index2.html'
    context_object_name = "crypto_list"

    def get_context_data(self, *args, **kwargs):
        data = super(WalletView, self).get_context_data(*args, **kwargs)
        return data


class WalletCreate(LoginRequiredMixin, CreateView):
    model = Wallet
    fields = ['coin_number', 'coin_type']
    template_name = 'index2_form.html'

    def get_success_url(self):
        return reverse('crypto:listare')

@login_required
def del_coin(request, pk):
    moneda = Wallet.objects.filter(id=pk)
    moneda.delete()
    return redirect('crypto:listare')

class Edit_coin(LoginRequiredMixin ,UpdateView):
    model = Wallet
    fields = ['coin_number', 'coin_type']
    template_name = 'index2_form.html'

    def get_success_url(self):
        return reverse('crypto:listare')
#queri
# def suma(request):
#     adunare_coin = Wallet.objects.all().aggregate(Sum())
#     return adunare_coin
