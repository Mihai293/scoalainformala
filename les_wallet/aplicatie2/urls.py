from django.urls import path
from . import views

app_name = 'wallet_pag'

urlpatterns = [
    path('', views.wallet, name='wallet'),
]