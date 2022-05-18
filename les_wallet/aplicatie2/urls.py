from django.urls import path
from . import views

urlpatterns = [
    path('wallet.html', views.wallet, name='wallet'),
]