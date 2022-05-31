from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView


from coinmarket_api.models import Wallet


@login_required
def coin(request):
    apidata = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    return render(request, 'index.html', {'apidata': apidata})


class WalletView(LoginRequiredMixin, ListView):
    model = Wallet
    template_name = 'index2.html'

    def get_context_data(self, *args, **kwargs):
        data = super(WalletView, self).get_context_data(*args, **kwargs)
        data['crypto_list'] = self.model.objects.filter(active=0)
        return data


class WalletCreate(LoginRequiredMixin, CreateView):
    model = Wallet
    fields = ['coin_number', 'coin_type']
    template_name = 'index2.html'

    def get_success_url(self):
        return reverse('crypto:add')

# class UpdateCompanyView(LoginRequiredMixin, UpdateView):
#     model = Wallet
#     fields = ['Coin', 'Valoare']
#     template_name = 'coinmarket_api/index2.html'
#
#     def get_success_url(self):
#         return reverse('coin:listare')
#
#
# @login_required
# def delete_coin(request, pk):
#     Companies.objects.filter(id=pk).update(active=0)
#     return redirect('companies:listare')
#
#
# @login_required
# def activate_company(request, pk):
#     Companies.objects.filter(id=pk).update(active=1)
#     return redirect('companies:listare')
#
#
# class CompanyInactiveView(LoginRequiredMixin, ListView):
#     model = Companies
#     template_name = 'aplicatie2/Companies_index.html'
#
#     def get_context_data(self, *args, **kwargs):
#         data = super(CompanyInactiveView, self).get_context_data(*args, **kwargs)
#         data['companies_list'] = self.model.objects.filter(active=0)
#         return data
